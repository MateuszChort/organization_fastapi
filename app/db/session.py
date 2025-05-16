from sqlmodel import Session, create_engine

DATABASE_URL = "sqlite:///./test.db"  # później zamienimy na PostgreSQL

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
