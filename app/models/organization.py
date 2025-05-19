from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.common import AddressKind, Location, Organization


class OrganizationAddressLink(SQLModel, table=True):
    organization_id: Optional[int] = Field(
        default=None, foreign_key="organization.id", primary_key=True
    )
    address_id: Optional[int] = Field(
        default=None, foreign_key="address.id", primary_key=True
    )


class Address(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    zip_code: str = Field(max_length=10)
    address: str = Field(max_length=255)

    location_id: int = Field(foreign_key="location.id")
    kind_id: int = Field(foreign_key="address_kind.id")

    location: Optional["Location"] = Relationship()
    kind: Optional["AddressKind"] = Relationship()

    organizations: List["Organization"] = Relationship(
        back_populates="addresses", link_model=OrganizationAddressLink
    )


class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    nip: str = Field(max_length=10)
    regon: str = Field(max_length=14)
    krs: Optional[str] = Field(default=None, max_length=10)

    # ManyToMany: Address
    addresses: List["Address"] = Relationship(
        back_populates="organizations", link_model=OrganizationAddressLink
    )

    # OneToMany: BankAccount
    bank_accounts: List["BankAccount"] = Relationship(back_populates="organization")

    @property
    def main_account(self) -> Optional["BankAccount"]:
        return next((ba for ba in self.bank_accounts if ba.main_account), None)
