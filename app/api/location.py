from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.crud import common as crud
from app.db.session import get_session
from app.models.common import Location
from app.schemas.common import LocationCreate, LocationRead, LocationUpdate

router = APIRouter()


@router.get("/", response_model=list[LocationRead])
def read_locations(session: Session = Depends(get_session)):
    return crud.get_all(session, Location)


@router.get("/{id}", response_model=LocationRead)
def read_location(id: int, session: Session = Depends(get_session)):
    item = crud.get_by_id(session, Location, id)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@router.post("/", response_model=LocationRead, status_code=201)
def create_location(data: LocationCreate, session: Session = Depends(get_session)):
    return crud.create(session, Location(**data.model_dump(exclude_unset=True)))


@router.put("/{id}", response_model=LocationRead)
def update_location(
    id: int, data: LocationUpdate, session: Session = Depends(get_session)
):
    item = crud.update(session, Location, id, data.model_dump(exclude_unset=True))
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@router.delete("/{id}")
def delete_location(id: int, session: Session = Depends(get_session)):
    item = crud.delete(session, Location, id)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": id}
