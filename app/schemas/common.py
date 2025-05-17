from pydantic import BaseModel


class AddressKindCreate(BaseModel):
    id: str
    kind: str


class AddressKindRead(AddressKindCreate):
    pass


class AddressKindUpdate(BaseModel):
    kind: str


class CurrencyCreate(BaseModel):
    code: str
    name: str


class CurrencyRead(CurrencyCreate):
    pass


class CurrencyUpdate(BaseModel):
    name: str
