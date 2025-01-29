from datetime import datetime
from enum import Enum

from sqlalchemy import (
    INTEGER,
    VARCHAR,
    Column,
    Enum as SQLAlchemyEnum,
    String,
    DateTime,
    ForeignKey,
    Uuid,
)
from database.config import Base


class TransactionTypeEnum(str, Enum):
    EXPENSE = "expense"
    INCOME = "income"


class TransactionModels(Base):
    __tablename__ = "transactions"  # Ensure the table name is specified

    transaction_id = Column(
        Uuid, primary_key=True, unique=True
    )  # Removed autoincrement for VARCHAR
    amount = Column(VARCHAR, nullable=False)
    description = Column(VARCHAR, nullable=True)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    type = Column(
        SQLAlchemyEnum(TransactionTypeEnum), nullable=False
    )  # Proper Enum usage
    user_id = Column(VARCHAR, ForeignKey("users.id"), nullable=False)
    category_id = Column(VARCHAR, ForeignKey("categories.category_id"), nullable=False)

    def __init__(
        self,
        amount: str,
        description: str,
        type: TransactionTypeEnum,
        user_id: Uuid,
        category_id: str,
    ):
        self.amount = amount
        self.description = description
        self.type = type
        self.user_id = user_id
        self.category_id = category_id  # Fixed assignment error

    def __repr__(self) -> str:
        return (
            f"<TransactionModel(amount={self.amount}, description={self.description}, "
            f"date={self.date}, type={self.type}, user_id={self.user_id}, category_id={self.category_id})>"
        )
