from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from alchemy import Base


engine = create_engine('postgresql+psycopg2://angelova:angelova@localhost:5432/tamriel_db')

Base.metadata.drop_all(engine)