from contextlib import contextmanager

import pyodbc
from sqlmodel import Session, create_engine

from src.settings import Settings

settings = Settings()

pyodbc.pooling = False

connection_string = 'mssql+pyodbc://{}:{}@{}/{}?TrustServerCertificate=yes&driver=ODBC+Driver+18+for+SQL+Server'.format(
    settings.MSSQL_USER,
    settings.MSSQL_SA_PASSWORD,
    settings.MSSQL_HOSTNAME,
    settings.APPLICATION_DB,
)

engine = create_engine(connection_string, pool_recycle=3600)

def get_session():
    with Session(engine, expire_on_commit=True) as session:
        yield session

session_context = contextmanager(get_session)