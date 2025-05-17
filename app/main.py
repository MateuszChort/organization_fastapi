from fastapi import FastAPI
from app.api import address_kind, currency
from app.db.session import engine
from sqlmodel import SQLModel

app = FastAPI()


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


app.include_router(address_kind.router, prefix="/address_kinds", tags=["AddressKind"])
app.include_router(currency.router, prefix="/currencies", tags=["Currency"])
