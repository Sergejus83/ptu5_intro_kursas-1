import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data_20221013/projektai.db')
Base = declarative_base()


class Projektas(Base):
    __tablename__ = 'projektas'
    id = Column(Integer, primary_key=True)
    name = Column("pavadinimas", String)
    price = Column("kaina", Float)
    created_date = Column("sukūrta", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.price}, {self.created_date})"


if __name__ == "__main__":
    Base.metadata.create_all(engine)