from sqlalchemy import MetaData, Table, Column, Integer,String,Boolean
from sqlalchemy.orm import DeclarativeBase
from fastapi_users.db import SQLAlchemyBaseUserTable

metadata = MetaData()

class Base(DeclarativeBase):
    pass

user = Table(
    'user',
    metadata,
    Column('id',Integer,primary_key=True),
    Column('username',String,nullable=False),
    Column('telegram_id',Integer),
    Column('subscription',Boolean,default=False),

    Column("email",String(length=320), unique=True, index=True, nullable=False),
    Column("hashed_password",String(length=1024), nullable=False),
    Column("is_active",Boolean, default=True, nullable=False),
    Column("is_superuser",Boolean, default=False, nullable=False),
    Column("is_verified",Boolean, default=False, nullable=False),

)


class User(SQLAlchemyBaseUserTable[int], Base):
    id:int = Column(Integer,primary_key=True)
    username:str = Column(String,nullable=False)
    telegram_id:int = Column(Integer)
    subscription:bool = Column(Boolean,default=False)
    
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)