from typing import Optional
from pydantic import BaseModel
from enum import Enum


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


class LocationKind(str, Enum):
    COUNTRY = "CR"
    REGION = "RG"
    CITY = "CT"


class LocationBase(BaseModel):
    name: str
    code: Optional[str] = None
    location_kind: Optional[LocationKind] = None
    parent_location_id: Optional[int] = None


class LocationCreate(LocationBase):
    pass


class LocationRead(LocationBase):
    id: int


class LocationUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    location_kind: Optional[LocationKind] = None
    parent_location_id: Optional[int] = None
