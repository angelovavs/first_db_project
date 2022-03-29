#from tamriel import filler
from pandas import read_json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
#from tamriel.alchemy import Base


engine = create_engine('postgresql+psycopg2://angelova:angelova@db:5432/tamriel_db')
conn=engine.connect()
print(conn)