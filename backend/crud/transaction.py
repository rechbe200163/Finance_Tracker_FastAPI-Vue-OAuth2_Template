from datetime import datetime

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.transactions import TransactionModels
import schemas.transaction


class TransactionCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def create_transaction(self, transaction: schemas.transaction.Base):
        db_transaction = TransactionModels(
            amount=transaction.amount,
            description=transaction.description,
            date=datetime.utcnow(),
            type=transaction.type,
            user_id=transaction.user_id,
            category_id=transaction.category_id,
        )
        self.db_session.add(db_transaction)
        await self.db_session.commit()
        return db_transaction

    async def update_amount(
        self, transaction_id: str, amount: schemas.transaction.Amount
    ):
        stmt = (
            update(TransactionModels)
            .where(TransactionModels.id == transaction_id)
            .values(amount=amount)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def update_description(
        self, transaction_id: str, description: schemas.transaction.Description
    ):
        stmt = (
            update(TransactionModels)
            .where(TransactionModels.id == transaction_id)
            .values(description=description)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def update_category(
        self, transaction_id: str, category_id: schemas.transaction.Category
    ):
        stmt = (
            update(TransactionModels)
            .where(TransactionModels.id == transaction_id)
            .values(category_id=category_id)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def updated_date(self, transaction_id: str, date: schemas.transaction.Date):
        stmt = (
            update(TransactionModels)
            .where(TransactionModels.id == transaction_id)
            .values(date=date)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def updated_type(self, transaction_id: str, type: schemas.transaction.Type):
        stmt = (
            update(TransactionModels)
            .where(TransactionModels.id == transaction_id)
            .values(type=type)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def get_transactions_by_user(self, user_id: str):
        stmt = select(TransactionModels).where(TransactionModels.user_id == user_id)
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions

    async def get_transactions_by_category(self, category_id: str):
        stmt = select(TransactionModels).where(
            TransactionModels.category_id == category_id
        )
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions
