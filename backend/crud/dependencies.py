from typing import Generator

from crud.category import CategoryCRUD
from crud.transaction import TransactionCRUD
from database.config import async_session
from crud.user import UserCRUD


async def get_db() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield session


async def get_user_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield UserCRUD(session)


async def get_transaction_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield TransactionCRUD(session)


async def get_category_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield CategoryCRUD(session)
