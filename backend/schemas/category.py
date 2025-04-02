from datetime import datetime
from pydantic import BaseModel

from models.db import CategoryTypeEnum

class BaseCategory(BaseModel):
    category_id: str


class CreateCategory(BaseModel):
    name: str
    type: CategoryTypeEnum

class UpdateCategoryType(BaseModel):
    type: str

class UpdateCategoryName(BaseModel):
    name: str

class ResponseCategory(BaseCategory):
    name: str
    type: CategoryTypeEnum
