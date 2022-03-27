from alchemy import Base, engine, Characters, Taglines, Stories, Battles
from datetime import date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import random

from pandas import read_json
from datetime import datetime

Session = sessionmaker(bind=engine)
#print(Session)

"""
Zurin_Arctus = Characters (
    name = "Zurin Arctus",
    side = "Imperial Legion",
    birthday = date(2002, 12, 31).isoformat(),
    strength = 70
)
"""


#with Session() as session:
#    for moto_id, moto in Zurin_Arctus_motos.items():
#        session.add(Taglines(hero_id=1, moto_id=moto_id, moto=moto))
#    session.commit()

"""

with Session() as session:
    session.add(Zurin_Arctus)
    session.commit()

with Session() as session:
    session.add(Zurin_Arctus_motos)
    session.commit()

with Session() as session:
    for moto in session.query(Taglines).all():
        print(moto)
        print(moto.character)
        print(moto.moto_id)


with Session() as session:
    for hero in session.query(Characters).all():
        print(hero)
        print(hero.birthday)
"""
tamriel_heroes = read_json('tamriel1.json', encoding='UTF-8')

class Fill_db:
    """Class to fill DataBase automatically (from json)"""

    def __init__(self, Session):
        self.Session = Session

    def __str__(self):
        return "fill_db_characters_auto - from json"

    def fill_db_characters_auto(self):
        with self.Session() as session:
            for hero_num in range(len(tamriel_heroes)):
                h_name=tamriel_heroes.loc[hero_num,'name']
                h_side=tamriel_heroes.loc[hero_num,'side']
                h_birthday=datetime.strptime(tamriel_heroes.loc[hero_num,'birthday'], "%d.%m.%Y")
                h_strength = tamriel_heroes.loc[hero_num,'strength']
                session.add(Characters(name=h_name, side=h_side, birthday=h_birthday, strength=int(h_strength)))

                h_id = session.query(Characters).filter(Characters.name == h_name).first()
                print('h_id', h_id)

                h_motos = tamriel_heroes.loc[hero_num,'motos']
                for moto_num, h_moto in h_motos.items():
                    print(moto_num, h_moto)
                    session.add(Taglines(moto_id=moto_num, moto=h_moto, hero_id=h_id.id))

                h_story=tamriel_heroes.loc[hero_num,'story']
                session.add(Stories(hero_id=h_id.id, story=h_story))
            session.commit()

    def fill_battles(self):
        with self.Session() as session:

            heroes_to_battle = session.query(Characters.id).all()
            print(heroes_to_battle)
            battle_hero_1_id = 3
            battle_tagline_1_id = session.query(Characters).filter(Characters.id == battle_hero_1_id).first().tagline[1].id
            battle_hero_2_id = 4
            battle_tagline_2_id = session.query(Characters).filter(Characters.id == battle_hero_1_id).first().tagline[1].id
            session.add(Battles(hero_1_id=battle_hero_1_id, hero_1_moto_id=battle_tagline_1_id,  hero_2_id=battle_hero_2_id, hero_2_moto_id=battle_tagline_2_id))

            #session.add(Battles(hero_1_id=77, hero_1_moto_id=1,  hero_2_id=12, hero_2_moto_id=55))

            session.commit()
