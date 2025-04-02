from datetime import datetime

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.db import CategoryModel, CategoryTypeEnum, UserModel
import schemas.category as cat_schema


class CategoryCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def create_category(self, transaction: cat_schema.CreateCategory, username: str):
        # Fetch the UserModel based on the username
        user_result = await self.db_session.execute(select(UserModel).where(UserModel.username == username))
        
        # Extract the first result (user instance)
        user = user_result.scalar_one_or_none()  # Returns None if no user is found
        
        # Check if the user was found
        if not user:
            raise ValueError("User not found")
        
        # Create the CategoryModel instance
        db_transaction = CategoryModel(
            name=transaction.name,
            type=transaction.type,
            user=user,  # Pass the user object
            username=username
        )

        # Add to session and commit
        self.db_session.add(db_transaction)
        await self.db_session.commit()

        return db_transaction


    async def get_category_by_name(self, name_pattern: str):
        stmt = select(CategoryModel).where(CategoryModel.name.like(f"%{name_pattern}%"))
        result = await self.db_session.execute(stmt)
        return result.scalars().all()

    async def get_category_by_type(self, type: CategoryTypeEnum):
        stmt = select(CategoryModel).where(CategoryModel.type == type)
        result = await self.db_session.execute(stmt)
        todos = result.scalars().all()
        return [cat_schema.ResponseCategory(**cat.__dict__) for cat in todos]

    async def get_categories(self, username: str):
        stmt = select(CategoryModel).where(CategoryModel.username == username)
        result = await self.db_session.execute(stmt)
        categories = result.scalars().all()
        return [cat_schema.ResponseCategory(**cat.__dict__) for cat in categories]
    
    async def get_category_by_id(self, category_id: str):
        stmt = select(CategoryModel).where(CategoryModel.category_id == category_id)
        result = await self.db_session.execute(stmt)
        return result.scalars().first

    async def update_name(
        self, category_id: str, name: cat_schema.UpdateCategoryName
    ):
        stmt = (
            update(CategoryModel)
            .where(CategoryModel.category_id == category_id)
            .values(name=name)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)


    async def update_type(self, category_id: str, type: cat_schema.UpdateCategoryType):
        stmt = (
            update(CategoryModel)
            .where(CategoryModel.category_id == category_id)
            .values(type=type)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_category(self, category_id: str):
        stmt = delete(CategoryModel).where(CategoryModel.category_id == category_id)
        await self.db_session.execute(stmt)
        await self.db_session.commit()
        return category_id
