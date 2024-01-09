from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, scoped_session

sqlite_database = 'sqlite:///pars.db'

engine = create_engine(sqlite_database)
db_session = scoped_session(sessionmaker(bind=engine))


class Base(DeclarativeBase): pass
