from sqlalchemy import Column, Integer, String, Float, ForeignKey

from bd_pars import Base, engine


class Pars(Base):
    __tablename__ = 'pars_offer'

    id = Column(Integer(), primary_key=True)
    rooms = Column(Integer())
    area = Column(Float())
    price = Column(Integer())
    address = Column(String())
    district = Column(String())
    floor = Column(Integer())
    url = Column(String(), unique=True)
    type = Column(String())

    def __init__(self):
        pass


if __name__ == '__main__':
    Base
