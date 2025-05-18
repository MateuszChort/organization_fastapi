from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.db.session import get_session
from app.models.organization import Organization, Address
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationRead,
    OrganizationUpdate,
)

router = APIRouter()


@router.get("/", response_model=List[OrganizationRead])
def get_organizations(session: Session = Depends(get_session)):
    return session.exec(select(Organization)).all()


@router.get("/{org_id}", response_model=OrganizationRead)
def get_organization(org_id: int, session: Session = Depends(get_session)):
    org = session.get(Organization, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org


@router.post("/", response_model=OrganizationRead, status_code=201)
def create_organization(
    data: OrganizationCreate, session: Session = Depends(get_session)
):
    org = Organization(
        name=data.name,
        nip=data.nip,
        regon=data.regon,
        krs=data.krs,
    )

    session.add(org)
    session.commit()
    session.refresh(org)

    if data.address_ids:
        addresses = session.exec(
            select(Address).where(Address.id.in_(data.address_ids))
        ).all()
        org.addresses = addresses
        session.add(org)
        session.commit()
        session.refresh(org)

    return org


@router.put("/{org_id}", response_model=OrganizationRead)
def update_organization(
    org_id: int, data: OrganizationUpdate, session: Session = Depends(get_session)
):
    org = session.get(Organization, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")

    org_data = data.dict(exclude_unset=True, exclude={"address_ids"})

    for key, value in org_data.items():
        setattr(org, key, value)

    if data.address_ids is not None:
        addresses = session.exec(
            select(Address).where(Address.id.in_(data.address_ids))
        ).all()
        org.addresses = addresses

    session.add(org)
    session.commit()
    session.refresh(org)
    return org


@router.delete("/{org_id}", status_code=204)
def delete_organization(org_id: int, session: Session = Depends(get_session)):
    org = session.get(Organization, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")

    session.delete(org)
    session.commit()
