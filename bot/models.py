from sqlalchemy import BigInteger, Column
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    chat_id: int = Field(sa_column=Column(BigInteger(), unique=True))