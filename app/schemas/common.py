from enum import Enum
from typing import Optional

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


class BankAccountBase(BaseModel):
    number: str
    is_active: bool = True
    main_account: bool = False
    currency_code: str
    organization_id: Optional[int] = None


class BankAccountCreate(BankAccountBase):
    pass


class BankAccountRead(BankAccountBase):
    id: int


class BankAccountUpdate(BaseModel):
    number: Optional[str] = None
    is_active: Optional[bool] = None
    main_account: Optional[bool] = None
    currency_code: Optional[str] = None
    organization_id: Optional[int] = None
