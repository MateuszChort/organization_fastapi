from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.models.common import BankAccount
from app.schemas.common import BankAccountCreate, BankAccountRead, BankAccountUpdate
from app.crud import common as crud

router = APIRouter()


@router.get("/", response_model=list[BankAccountRead])
def read_accounts(session: Session = Depends(get_session)):
    return crud.get_all(session, BankAccount)


@router.get("/{id}", response_model=BankAccountRead)
def read_account(id: int, session: Session = Depends(get_session)):
    account = crud.get_by_id(session, BankAccount, id)
    if not account:
        raise HTTPException(status_code=404, detail="Not found")
    return account


@router.post("/", response_model=BankAccountRead)
def create_account(data: BankAccountCreate, session: Session = Depends(get_session)):
    return crud.create(session, BankAccount(**data.dict()))


@router.put("/{id}", response_model=BankAccountRead)
def update_account(
    id: int, data: BankAccountUpdate, session: Session = Depends(get_session)
):
    account = crud.update(session, BankAccount, id, data.dict(exclude_unset=True))
    if not account:
        raise HTTPException(status_code=404, detail="Not found")
    return account


@router.delete("/{id}")
def delete_account(id: int, session: Session = Depends(get_session)):
    account = crud.delete(session, BankAccount, id)
    if not account:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": id}
