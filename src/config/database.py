from contextlib import contextmanager
from sqlmodel import SQLModel, Session, create_engine

PG_USERNAME = "postgres"
PG_PASSWORD = "postgres"
PG_HOST = "localhost"
PG_PORT = 5433
PG_DATABASE = "postgres"

connect_args = {}
db_url = f"postgresql://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"

engine = create_engine(db_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_engine():
    return engine

@contextmanager
def get_session():
    yield Session(engine)