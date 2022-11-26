import os

from sqlmodel import SQLModel, create_engine, Session


DB_USER = os.environ.get('MYSQL_USER')
DB_PASSWORD = os.environ.get('MYSQL_PASSWORD')
DB_HOST = os.environ.get('MYSQL_HOST')
DB_PORT = os.environ.get('MYSQL_PORT')
DB_NAME = os.environ.get('MYSQL_DATABASE')

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
    DB_USER,
    DB_PASSWORD,
    f'{DB_HOST}:{DB_PORT}',
    DB_NAME,
)

engine = create_engine(DATABASE, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
