from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from auth.action import get_current_user
from crud.transaction import TransactionCRUD
from crud.dependencies import get_transaction_crud
import schemas.transaction as transaction_crud
import schemas.user as user_schema
import schemas.transaction as tr_schema

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.get("", response_model=List[tr_schema.ResponseTransaction])
async def get_transactions(
    description: str = None,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        print("User not found")
        raise HTTPException(status_code=401, detail="Unauthorized")
    if description:
        return await db.get_transactions_by_description(current_user.username, description)
    return await db.get_transactions_by_user(current_user.username)

@router.get("/{transaction_id}", response_model=tr_schema.ResponseTransaction)
async def get_transaction_by_id(
    transaction_id: str,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.get_transaction_by_id(transaction_id)


#transactions by category
@router.get("/category/{category_id}", response_model=List[tr_schema.ResponseTransaction])
async def get_transactions_by_categoryid(
    category_id: str,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.get_transactions_by_category(category_id)

#by amount
@router.get("/amount/{amount}", response_model=List[tr_schema.ResponseTransaction])
async def get_transactions_by_amount(
    amount: float,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.get_transactions_by_amount(amount)

#by type
@router.get("/type/{type}", response_model=List[tr_schema.ResponseTransaction])
async def get_transactions_by_type(
    type: str,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.get_transactions_by_type(type)

#by date range using start_date and end_date as query parameters
@router.get("/date", response_model=List[tr_schema.ResponseTransaction])
async def get_transactions_by_date_range(
    start_date: str,
    end_date: str,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.get_transactions_by_date_range(start_date, end_date)

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_transaction(
    new_transaction:tr_schema.CreateTransaction,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.create_transaction(new_transaction, current_user.username)

@router.patch("/{transaction_id}/amount", status_code=status.HTTP_200_OK)
async def update_amount(
    transaction_id: str,
    update_data: tr_schema.UpdateTransactionAmount,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.update_amount(transaction_id, update_data.amount)

@router.patch("/{transaction_id}/description", status_code=status.HTTP_200_OK)
async def update_description(
    transaction_id: str,
    update_data: tr_schema.UpdateTransactionDescription,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.update_description(transaction_id, update_data.description)

@router.patch("/{transaction_id}/category", response_model=tr_schema.ResponseTransaction)
async def update_category(
    transaction_id: str,
    update_data: tr_schema.UpdateTransactionCategory,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.update_category(transaction_id, update_data.category_id)

@router.patch("/{transaction_id}/date", response_model=tr_schema.ResponseTransaction)
async def update_date(
    transaction_id: str,
    update_data: tr_schema.UpdateTransactionDate,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.update_date(transaction_id, update_data.date)

@router.patch("/{transaction_id}/type", status_code=status.HTTP_200_OK)
async def update_type(
    transaction_id: str,
    update_data: tr_schema.UpdateTransactionType,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.update_type(transaction_id, update_data.type)

@router.delete("/{transaction_id}", status_code=status.HTTP_200_OK)
async def delete_transaction(
    transaction_id: str,
    db: TransactionCRUD = Depends(get_transaction_crud),
    current_user: user_schema.Base = Depends(get_current_user),
):
    print('here')
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await db.delete_transaction(transaction_id)