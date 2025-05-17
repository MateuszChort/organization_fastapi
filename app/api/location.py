from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.models.common import Location
from app.schemas.common import LocationCreate, LocationRead, LocationUpdate
from app.crud import common as crud

router = APIRouter()


@router.get("/", response_model=list[LocationRead])
def read_locations(session: Session = Depends(get_session)):
    return crud.get_all_locations(session)


@router.get("/{id}", response_model=LocationRead)
def read_location(id: int, session: Session = Depends(get_session)):
    item = crud.get_location(session, id)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@router.post("/", response_model=LocationRead)
def create_location(data: LocationCreate, session: Session = Depends(get_session)):
    return crud.create_location(session, Location(**data.dict()))


@router.put("/{id}", response_model=LocationRead)
def update_location(
    id: int, data: LocationUpdate, session: Session = Depends(get_session)
):
    item = crud.update_location(session, id, data.dict(exclude_unset=True))
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@router.delete("/{id}")
def delete_location(id: int, session: Session = Depends(get_session)):
    item = crud.delete_location(session, id)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": id}
