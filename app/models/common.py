from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from enum import Enum


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
