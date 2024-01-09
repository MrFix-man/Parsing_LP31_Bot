from models import Pars_db
from db_connect import db_session


pars_db = Pars_db(id=id, rooms=rooms, area=area, price=price,
        address=address, district=district, floor=floor,
        url=url, type=type)


def insert_pars():
    db_session.add(pars_db)
    db_session.commit()


def query_pars():
    db_session.query(all())