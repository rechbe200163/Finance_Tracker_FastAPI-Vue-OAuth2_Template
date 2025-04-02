from datetime import datetime
from pydantic import BaseModel

from models.db import TransactionTypeEnum

class BaseTransaction(BaseModel):
    transaction_id: str


class CreateTransaction(BaseModel):
    amount: int
    description: str
    date: datetime
    type: TransactionTypeEnum
    category_id: str

class UpdateTransactionAmount(BaseModel):
    amount: int

class UpdateTransactionDescription(BaseModel):
    description: str

class UpdateTransactionCategory(BaseModel):
    category_id: str

class UpdateTransactionDate(BaseModel):
    date: datetime

class UpdateTransactionType(BaseModel):
    type: TransactionTypeEnum

class ResponseTransaction(BaseTransaction):
    amount: int
    description: str
    date: datetime
    type: TransactionTypeEnum
    category_id: str
    username: str