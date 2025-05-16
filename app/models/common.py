from sqlmodel import SQLModel, Field
from typing import Optional


class AddressKind(SQLModel, table=True):
    id: str = Field(primary_key=True, max_length=20)
    kind: str
