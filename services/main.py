import filler
from pandas import read_json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from alchemy import Base, engine


#engine = create_engine('postgresql+psycopg2://angelova:angelova@localhost:5432/tamriel_db')
tamriel_heroes = read_json('tamriel1.json', encoding='UTF-8')
Session = sessionmaker(bind=engine)

#Base.metadata.create_all(engine)

fill_db = filler.Fill_db(Session)

#fill_db.fill_db_characters_auto()
#fill_db.fill_battles()


print(fill_db.__doc__)