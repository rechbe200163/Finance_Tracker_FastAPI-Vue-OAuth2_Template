from datetime import datetime

from sqlalchemy import INTEGER, Column, VARCHAR, DATE, DateTime, Uuid

from database.config import Base


# Create User class
class UserModels(Base):
    __tablename__ = "users"
    user_id = Column(Uuid, primary_key=True, unique=True)
    firstname = Column(VARCHAR)
    lastname = Column(VARCHAR)
    email = Column(VARCHAR)
    password = Column(VARCHAR)
    birthday = Column(DATE)
    create_time = Column(DateTime, default=datetime.utcnow())
    last_login = Column(DateTime, default=datetime.utcnow())

    def __init__(self, username: str, password: str, birthday: datetime, user_id: Uuid):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.birthday = birthday

    def __repr__(self) -> str:
        return f"<UserModels(username={self.username}, password={self.password}, birthday={self.birthday})>"
