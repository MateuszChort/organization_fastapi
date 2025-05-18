from pydantic import BaseModel
from typing import Optional, List


class AddressBase(BaseModel):
    zip_code: str
    address: str
    location_id: int
    kind_id: int


class AddressCreate(AddressBase):
    pass


class AddressRead(AddressBase):
    id: int


class AddressUpdate(BaseModel):
    zip_code: Optional[str] = None
    address: Optional[str] = None
    location_id: Optional[int] = None
    kind_id: Optional[int] = None


class OrganizationBase(BaseModel):
    name: str
    nip: str
    regon: str
    krs: Optional[str] = None
    address_ids: Optional[List[int]] = []  # do powiązań ManyToMany


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationRead(OrganizationBase):
    id: int


class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    nip: Optional[str] = None
    regon: Optional[str] = None
    krs: Optional[str] = None
    address_ids: Optional[List[int]] = None
