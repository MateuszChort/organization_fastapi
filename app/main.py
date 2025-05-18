from fastapi import FastAPI
from app.api import address_kind, currency, location, bank_account, organization
from app.db.session import engine
from sqlmodel import SQLModel

app = FastAPI()


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


app.include_router(address_kind.router, prefix="/address_kinds", tags=["AddressKind"])
app.include_router(currency.router, prefix="/currencies", tags=["Currency"])
app.include_router(location.router, prefix="/locations", tags=["Location"])
app.include_router(bank_account.router, prefix="/bank_accounts", tags=["BankAccount"])
app.include_router(organization.router, prefix="/organizations", tags=["Organization"])
