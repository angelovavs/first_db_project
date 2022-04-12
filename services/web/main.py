from tamriel import filler
from pandas import read_json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from tamriel.alchemy import Base


engine = create_engine('postgresql+psycopg2://angelova:angelova@localhost:5432/tamriel_db')
conn=engine.connect()
print(conn)

def create_db(engine):
    #engine = create_engine('postgresql+psycopg2://angelova:angelova@localhost:5432/tamriel_db')
    tamriel_heroes = read_json('tamriel.json', encoding='UTF-8')
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    fill_db = filler.Fill_db(Session)

def clear_db(engine):
    Base.metadata.drop_all(engine)
    print('db is cleared')

clear_db(engine)

#fill_db.fill_db_characters_auto()
#fill_db.fill_battles()
