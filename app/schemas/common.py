from pydantic import BaseModel


class AddressKindCreate(BaseModel):
    id: str
    kind: str


class AddressKindRead(AddressKindCreate):
    pass


class AddressKindUpdate(BaseModel):
    kind: str
