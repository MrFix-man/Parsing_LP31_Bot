from sqlalchemy import create_engine
from sqlalchemy.future import engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker


bd_sesion = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

Base.query = bd_sesion.query_property()
