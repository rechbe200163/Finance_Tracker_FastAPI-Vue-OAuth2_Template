from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from auth.action import get_current_user
from crud.transaction import TransactionCRUD
from crud.dependencies import get_user_crud
import schemas.transaction as transaction_crud

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("/", response_model=List[transaction_crud.BaseModel])
async def get_transactions_by_user_id(
    user_id: int, db: TransactionCRUD = Depends(get_user_crud)
):
    transactions = await db.get_transactions_by_user_id(user_id=user_id)
    if transactions is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Transactions not found"
        )
    return transactions
