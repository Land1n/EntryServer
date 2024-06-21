from sqlalchemy import MetaData, Table, Column, Integer,String,Boolean

metadata = MetaData()

User = Table(
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