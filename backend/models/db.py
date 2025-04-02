from typing import List
import uuid
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum as SQLAlchemyEnum, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.config import Base


# Enum for Category Types
class CategoryTypeEnum(str, Enum):
    SPORTS = "sports"
    SHOPPING = "shopping"
    FOOD = "food"
    TRANSPORT = "transport"
    BILLS = "bills"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"


# Enum for Transaction Types
class TransactionTypeEnum(str, Enum):
    EXPENSE = "expense"
    INCOME = "income"


# Create Transaction class
class TransactionModel(Base):
    __tablename__ = "transactions"

    transaction_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    type: Mapped[TransactionTypeEnum] = mapped_column(SQLAlchemyEnum(TransactionTypeEnum), nullable=False)
    username: Mapped[str] = mapped_column(String, ForeignKey("users.username"), nullable=False)
    
    # Change to one-to-many relationship: A category can have many transactions, but each transaction belongs to only one category
    category_id: Mapped[str] = mapped_column(String, ForeignKey('categories.category_id'), nullable=False)
    
    # Define the relationship from the transaction side
    category: Mapped['CategoryModel'] = relationship("CategoryModel", back_populates="transactions")

    user: Mapped['UserModel'] = relationship("UserModel", back_populates="transactions")

    def __init__(self, amount: float, description: str, type: TransactionTypeEnum, category_id: str, date: datetime = None, username: str = None, user: str = None):
        self.amount = amount
        self.description = description
        self.type = type
        self.date = date or datetime.utcnow()
        self.username = username
        self.user = user
        self.category_id = category_id  # Reference to the category_id

    def __repr__(self) -> str:
        return (
            f"<TransactionModel(amount={self.amount}, description={self.description}, "
            f"date={self.date}, type={self.type}, username={self.username})>"
        )


# Create Category class
class CategoryModel(Base):
    __tablename__ = "categories"

    category_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[CategoryTypeEnum] = mapped_column(SQLAlchemyEnum(CategoryTypeEnum), nullable=False)
    username: Mapped[str] = mapped_column(String, ForeignKey("users.username"), nullable=False)
    
    # One-to-many relationship: A category can have many transactions, but each transaction belongs to one category
    transactions: Mapped[List['TransactionModel']] = relationship("TransactionModel", back_populates="category")

    user: Mapped['UserModel'] = relationship("UserModel", back_populates="categories")

    def __init__(self, name: str, type: CategoryTypeEnum, user: str, username: str):
        self.name = name
        self.type = type
        self.user = user
        self.username = username

    def __repr__(self) -> str:
        return f"<CategoryModel(name={self.name}, type={self.type}, username={self.username}, user={self.user})>"


class UserModel(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column("username", unique=True, primary_key=True)
    password: Mapped[str] = mapped_column("password")
    birthday: Mapped[datetime] = mapped_column("birthday")
    create_time: Mapped[datetime] = mapped_column(
        "create_time", default=datetime.utcnow()
    )
    last_login: Mapped[datetime] = mapped_column(
        "last_login", default=datetime.utcnow()
    )
    categories: Mapped[List['CategoryModel']] = relationship("CategoryModel", back_populates="user")
    transactions: Mapped[List['TransactionModel']] = relationship("TransactionModel", back_populates="user")

    def __init__(
        self,
        username: str,
        password: str,
        birthday: datetime = None,
    ):
        self.username = username
        self.password = password
        self.birthday = birthday

    def __repr__(self) -> str:
        return (
            f"<UserModel(firstname={self.firstname}, lastname={self.lastname}, "
            f"email={self.email}, birthday={self.birthday})>"
        )
