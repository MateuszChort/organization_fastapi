from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from enum import Enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.organization import Organization


class AddressKind(SQLModel, table=True):
    id: str = Field(primary_key=True, max_length=20)
    kind: str


class Currency(SQLModel, table=True):
    code: str = Field(primary_key=True, max_length=3)
    name: str


class LocationKind(str, Enum):
    COUNTRY = "CR"
    REGION = "RG"
    CITY = "CT"


class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    code: Optional[str] = None
    location_kind: Optional[LocationKind] = Field(default=None)
    parent_location_id: Optional[int] = Field(default=None, foreign_key="location.id")

    parent_location: Optional["Location"] = Relationship(
        back_populates="child_locations",
        sa_relationship_kwargs={"remote_side": "Location.id"},
    )
    child_locations: list["Location"] = Relationship(back_populates="parent_location")


class BankAccount(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    number: str = Field(index=True, unique=True)
    is_active: bool = True
    main_account: bool = False

    currency_code: str = Field(foreign_key="currency.code")
    organization_id: Optional[int] = Field(default=None, foreign_key="organization.id")

    currency: Optional[Currency] = Relationship()
    organization: Optional["Organization"] = Relationship(
        back_populates="bank_accounts"
    )
