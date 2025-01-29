from pydantic import BaseModel


class Category(BaseModel):
    category_id: str


class Base(Category):
    amount: float
    desciption: str
    date: str
    type: str
    user_id: str


class Amount(Base):
    amount: float


class Description(Base):
    description: str


class Date(Base):
    date: str


class Type(Base):
    type: str
