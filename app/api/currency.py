from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.crud import common as crud
from app.db.session import get_session
from app.models.common import Currency
from app.schemas.common import CurrencyCreate, CurrencyRead, CurrencyUpdate

router = APIRouter()


@router.get("/", response_model=list[CurrencyRead])
def read_currencies(session: Session = Depends(get_session)):
    return crud.get_all(session, Currency)


@router.get("/{code}", response_model=CurrencyRead)
def read_currency(code: str, session: Session = Depends(get_session)):
    item = crud.get_by_id(session, Currency, code)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@router.post("/", response_model=CurrencyRead, status_code=201)
def create_currency(data: CurrencyCreate, session: Session = Depends(get_session)):
    return crud.create(session, Currency(**data.dict(exclude_unset=True)))


@router.put("/{code}", response_model=CurrencyRead)
def update_currency(
    code: str, data: CurrencyUpdate, session: Session = Depends(get_session)
):
    item = crud.update(session, Currency, code, data.dict(exclude_unset=True))
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@router.delete("/{code}")
def delete_currency(code: str, session: Session = Depends(get_session)):
    item = crud.delete(session, Currency, code)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": code}
