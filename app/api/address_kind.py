from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.crud import common as crud
from app.db.session import get_session
from app.models.common import AddressKind
from app.schemas.common import AddressKindCreate, AddressKindRead, AddressKindUpdate

router = APIRouter()


@router.get("/", response_model=list[AddressKindRead])
def read_address_kinds(session: Session = Depends(get_session)):
    return crud.get_all(session, AddressKind)


@router.post("/", response_model=AddressKindRead, status_code=201)
def create_address_kind(
    data: AddressKindCreate, session: Session = Depends(get_session)
):
    return crud.create(session, AddressKind(**data.model_dump()))


@router.get("/{id}", response_model=AddressKindRead)
def read_address_kind(id: str, session: Session = Depends(get_session)):
    item = crud.get_by_id(session, AddressKind, id)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@router.put("/{id}", response_model=AddressKindRead)
def update_address_kind(
    id: str, data: AddressKindUpdate, session: Session = Depends(get_session)
):
    item = crud.update(session, AddressKind, id, data.model_dump(exclude_unset=True))
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@router.delete("/{id}")
def delete_address_kind(id: str, session: Session = Depends(get_session)):
    item = crud.delete(session, AddressKind, id)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": id}
