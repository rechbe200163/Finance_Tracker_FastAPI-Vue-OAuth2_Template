from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from auth.action import get_current_user
from models.db import CategoryTypeEnum
from crud.category import CategoryCRUD
from crud.dependencies import get_category_crud
import schemas.user as user_schema
import schemas.category as cat_schema

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("", response_model=List[cat_schema.ResponseCategory])
async def get_categories(
    db: CategoryCRUD = Depends(get_category_crud),
    current_user: user_schema.Base  = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.get_categories(current_user.username)

@router.get("/{category_id}", response_model=cat_schema.ResponseCategory)
async def get_category_by_id(
    category_id: str,
    db: CategoryCRUD = Depends(get_category_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.get_category_by_id(category_id)

# get by name
@router.get("/name/{name}", response_model=List[cat_schema.ResponseCategory])
async def get_category_by_name(
    name: str,
    db: CategoryCRUD = Depends(get_category_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.get_category_by_name(name)

# get by type

@router.get("/type/{type}", response_model=List[cat_schema.ResponseCategory])
async def get_category_by_type(
    type: CategoryTypeEnum,
    db: CategoryCRUD = Depends(get_category_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.get_category_by_type(type)

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_category(
    new_transaction:cat_schema.CreateCategory,
    db: CategoryCRUD = Depends(get_category_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    # Check if the category already exists
    existing_category = await db.get_category_by_name(new_transaction.name)
    if existing_category:
        raise HTTPException(status_code=409, detail="Category already exists")
    return await db.create_category(new_transaction, current_user.username)

@router.put("update/name/{category_id}", status_code=status.HTTP_200_OK)
async def update_name(
    category_id: str,
    update_data: cat_schema.UpdateCategoryName,
    db: CategoryCRUD = Depends(get_category_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.update_name(category_id, update_data.name)

@router.put("update/type/{category_id}", status_code=status.HTTP_200_OK)
async def update_type(
    category_id: str,
    update_data: cat_schema.UpdateCategoryType,
    db: CategoryCRUD = Depends(get_category_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.update_type(category_id, update_data.type)

@router.delete("/{category_id}", status_code=status.HTTP_200_OK)
async def delete_category(
    category_id: str,
    db: CategoryCRUD = Depends(get_category_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.delete_category(category_id)

