from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ParsAvito(Base):
    __tablename__ = 'pars_avito'

    id = Column(Integer(), primary_key=True)
    avito_id = Column(Integer(), unique=True)
    rooms = Column(String(5))
    area = Column(Float(5))
    price = Column(String(20))
    adress = Column(String())
    district = Column(String())
    floor_level = Column(String())
    url_offer = Column(String(), unique=True)
    type = Column(String())


class ParsDrom(Base):
    __tablename__ = 'pars_drom'

    id = Column(Integer(), primary_key=True)
    url_cars = Column(String(), unique=True)
    car_name = Column(String(25))
    car_year = Column(Integer())
    short_descript = Column(String())
    price_int = Column(Integer())
    town = Column(String())
    day_of_announcement = Column(String())
    site_evaluation = Column(String())
    type = Column(String())

