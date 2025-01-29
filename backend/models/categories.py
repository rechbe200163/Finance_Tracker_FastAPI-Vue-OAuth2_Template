from datetime import datetime
from sqlalchemy import (
    INTEGER,
    VARCHAR,
    Column,
    Enum as SQLAlchemyEnum,
    ForeignKey,
    Uuid,
)
from database.config import Base
from enum import Enum


class CategoryTypeEnum(str, Enum):
    SPORTS = "sports"
    SHOPPING = "shopping"
    FOOD = "food"
    TRANSPORT = "transport"
    BILLS = "bills"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"


class CategoryModels(Base):
    __tablename__ = "categories"  # Fixed typo

    category_id = Column(
        Uuid, primary_key=True, unique=True
    )  # Removed autoincrement for VARCHAR
    name = Column(VARCHAR, nullable=False)
    type = Column(SQLAlchemyEnum(CategoryTypeEnum), nullable=False)  # Proper Enum usage
    user_id = Column(INTEGER, ForeignKey("users.id"), nullable=False)

    def __init__(self, name: str, type: CategoryTypeEnum, user_id: Uuid):
        self.name = name
        self.type = type
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"<CategoryModels(name={self.name}, type={self.type}, user_id={self.user_id})>"
