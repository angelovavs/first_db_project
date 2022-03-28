from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy_backup import Characters, Stories, Battles


engine = create_engine('postgresql+psycopg2://angelova:angelova@localhost:5432/tamriel_db')

Session = sessionmaker(bind=engine)

with Session() as session:
    char_to_del = session.query(Characters).filter(Characters.name == 'Larrius Varro').first()
    #char_to_del = session.query(Battles).filter(Battles.id == 1).first()
    session.delete(char_to_del)
    session.commit()


#user1 = sess.query(User).filter_by(id=1).first()
#sess.delete(user1)