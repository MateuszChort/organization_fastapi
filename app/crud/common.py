from sqlmodel import Session, select
from app.models.common import AddressKind


def get_all_address_kinds(session: Session):
    return session.exec(select(AddressKind)).all()


def get_address_kind(session: Session, id: str):
    return session.get(AddressKind, id)


def create_address_kind(session: Session, data: AddressKind):
    session.add(data)
    session.commit()
    session.refresh(data)
    return data


def delete_address_kind(session: Session, id: str):
    item = session.get(AddressKind, id)
    if item:
        session.delete(item)
        session.commit()
    return item


def update_address_kind(session: Session, id: str, data: dict):
    item = session.get(AddressKind, id)
    if not item:
        return None
    for key, value in data.items():
        setattr(item, key, value)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
