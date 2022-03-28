from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, text
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://angelova:angelova@localhost:5432/tamriel_db')
conn = engine.connect()

Base = declarative_base()


class Characters(Base):
    __tablename__ = "characters"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    side = Column(String(100))
    name = Column(String(100), unique=True)
    birthday = Column(DateTime(timezone=True))
    strength = Column(Integer)
    update_dttm = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    tagline = relationship("Taglines", back_populates="character", cascade = "all,delete")
    stories = relationship("Stories", back_populates="character", cascade = "all,delete")

    def __repr__(self):
        return f"{self.id}: {self.name}"


class Taglines(Base):
    __tablename__ = "taglines"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey("characters.id" , ondelete="CASCADE"))
    character = relationship("Characters", back_populates="tagline")
    moto_id = Column(Integer)
    moto = Column(String(200))

    def __repr__(self):
        return f"{self.id}: {self.moto}"

class Stories(Base):
    __tablename__ = "stories"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"), unique=True)
    character = relationship("Characters", back_populates="stories")
    story = Column(String(1000))

    def __repr__(self):
        return f"{self.hero_id}: {self.story}"

class Battles(Base):
    __tablename__ = "battles"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    hero_1_id = Column(Integer)  # Герой 1 - тот, кто инициировал столкновение
    hero_1_moto_id = Column(Integer)
    hero_2_id = Column(Integer)
    hero_2_moto_id = Column(Integer)
    winner = Column(Integer)  # (0 для ничьей, 1 для героя 1, 2 для героя 2)

    def __repr__(self):
        return f"{self.id}: {self.winner}"


Base.metadata.create_all(engine)

