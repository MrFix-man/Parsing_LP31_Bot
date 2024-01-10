from models import Pars_db
from db_connect import db_session
from sqlalchemy import select


def insert_pars(all_offers):
    for offers in all_offers:
        pars_db = Pars_db(avito_id=offers['avito_id'],
                          rooms=offers['rooms'],
                          area=offers['area'],
                          price=offers['price'],
                          address=offers['address'],
                          district=offers['district'],
                          floor=offers['floor'],
                          url=offers['url'],
                          type=offers['type'])

        db_session.add(pars_db)
    db_session.commit()


def query_pars():
    all_data = db_session.execute(select(Pars_db)).scalars().all()
    return all_data
