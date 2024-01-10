from sqlalchemy import Column, Integer, String, Float

from db_connect import engine, Base

class Pars_db(Base):
    __tablename__ = 'pars_db'

    id = Column(Integer(), primary_key=True)
    avito_id = Column(Integer())
    rooms = Column(Integer())
    area = Column(Float())
    price = Column(Integer())
    address = Column(String())
    district = Column(String())
    floor = Column(Integer())
    url = Column(String(), unique=True)
    type = Column(String())

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)