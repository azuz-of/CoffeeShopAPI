import enum

from sqlalchemy import Column, DateTime, Integer, Enum, String, Boolean
from sqlalchemy.orm import DeclarativeBase

from .helpers import now

class Base(DeclarativeBase):
    pass

class BaseModelMixin:
    created_at = Column(DateTime, default=now)
    updated_at = Column(DateTime, default=now)

class UserRole(enum.Enum):
    ADMIN = 'admin'
    USER = 'user'

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    role = Column(Enum(UserRole), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    is_verified = Column(Boolean, nullable=False, default=False)
    token = Column(String(255), nullable=False)
    token_expires = Column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"<User id={self.id} role={self.role} email={self.email}> is_verified={self.is_verified}>"
