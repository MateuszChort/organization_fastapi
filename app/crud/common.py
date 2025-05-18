from sqlmodel import Session, select
from typing import Type, TypeVar, Optional

ModelType = TypeVar("ModelType")


def get_all(session: Session, model: Type[ModelType]) -> list[ModelType]:
    return session.exec(select(model)).all()


def get_by_id(
    session: Session, model: Type[ModelType], id: int | str
) -> Optional[ModelType]:
    return session.get(model, id)


def create(session: Session, instance: ModelType) -> ModelType:
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return instance


def update(
    session: Session, model: Type[ModelType], id: int | str, data: dict
) -> Optional[ModelType]:
    item = session.get(model, id)
    if not item:
        return None
    for key, value in data.items():
        setattr(item, key, value)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def delete(
    session: Session, model: Type[ModelType], id: int | str
) -> Optional[ModelType]:
    item = session.get(model, id)
    if item:
        session.delete(item)
        session.commit()
    return item
