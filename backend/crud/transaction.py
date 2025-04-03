from datetime import datetime

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.db import CategoryModel, TransactionModel, UserModel
import schemas.transaction as tr_schema


class TransactionCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def create_transaction(self, transaction: tr_schema.CreateTransaction, username: str):
        stmt = select(UserModel).where(UserModel.username == username)
        result = await self.db_session.execute(stmt)
        user = result.scalars().first()

        db_transaction = TransactionModel(
            amount=transaction.amount,
            description=transaction.description,
            date=datetime.utcnow(),
            type=transaction.type,
            username=username,
            user=user,
            category_id=transaction.category_id
        )   
        self.db_session.add(db_transaction)
        await self.db_session.commit()
        return db_transaction

    async def update_amount(
        self, transaction_id: str, amount: tr_schema.UpdateTransactionAmount
    ):
        stmt = (
            update(TransactionModel)
            .where(TransactionModel.transaction_id == transaction_id)
            .values(amount=amount)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def update_description(
        self, transaction_id: str, description: tr_schema.UpdateTransactionDescription
    ):
        stmt = (
            update(TransactionModel)
            .where(TransactionModel.transaction_id == transaction_id)
            .values(description=description)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def update_category(
        self, transaction_id: str, category_id: tr_schema.UpdateTransactionCategory
    ):
        stmt = (
            update(TransactionModel)
            .where(TransactionModel.transaction_id == transaction_id)
            .values(category_id=category_id)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def update_date(self, transaction_id: str, date: tr_schema.UpdateTransactionDate):
        stmt = (
            update(TransactionModel)
            .where(TransactionModel.transaction_id == transaction_id)
            .values(date=date)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def update_type(self, transaction_id: str, type: tr_schema.UpdateTransactionType):
        stmt = (
            update(TransactionModel)
            .where(TransactionModel.transaction_id == transaction_id)
            .values(type=type)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def get_transaction_by_id(self, transaction_id: str) -> tr_schema.ResponseTransaction:
        stmt = select(TransactionModel).where(TransactionModel.transaction_id == transaction_id)
        result = await self.db_session.execute(stmt)
        transaction = result.scalars().first()
        return transaction
    
    async def get_transactions(self):
        stmt = select(TransactionModel)
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return [tr_schema.ResponseTransaction(**transaction.__dict__) for transaction in transactions]
    

    async def get_transactions_by_amount(self, amount: float):
        stmt = select(TransactionModel).where(TransactionModel.amount == amount)
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions

    async def get_transactions_by_type(self, type: str):
        stmt = select(TransactionModel).where(TransactionModel.type == type)
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions
    
    async def get_transactions_by_date_range(self, start_date: datetime, end_date: datetime):
        stmt = select(TransactionModel).where(
            TransactionModel.date >= start_date,
            TransactionModel.date <= end_date
        )
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions

    async def get_transactions_by_user(self, username: str):
        stmt = select(TransactionModel).where(TransactionModel.username == username)
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions

    async def get_transactions_by_category(self, category_id: str):
        stmt = select(TransactionModel).where(
            TransactionModel.categories.any(CategoryModel.category_id == category_id)
        )
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions

    async def get_transactions_by_description(self, username: str, description: str):
        stmt = select(TransactionModel).where(
            TransactionModel.username == username,
            TransactionModel.description.ilike(f"%{description}%")
        )
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions    

    async def delete_transaction(self, transaction_id: str):
        stmt = delete(TransactionModel).where(TransactionModel.transaction_id == transaction_id)
        await self.db_session.execute(stmt)
        await self.db_session.commit()
        return {"message": "Transaction deleted successfully"}
