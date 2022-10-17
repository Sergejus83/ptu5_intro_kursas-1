import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data_20221013/darbotuojai.db')
Base = declarative_base()

class Darbuotojai(Base):
    __tablename__ = 'Darbotuojai'
    id = Column(Integer, primary_key=True)
    first_name = Column("Vardas", String)
    last_name = Column("Pavarde", String)
    birth_day = Column("Gimimo data", DateTime)
    position = Column("Pareigos", String)
    salary = Column("Atlyginimas", Float)
    work_from = Column("Dirba nuo",DateTime, default=datetime.datetime.now)

    def __init__(self, first_name, last_name, birth_day, position, salary, work_from):
        self.first_name=first_name
        self.last_name=last_name
        self.birth_day=birth_day
        self.position=position
        self.salary=salary
        self.work_from=work_from


    def __repr__(self):
        return f"({self.id}, {self.first_name}, {self.last_name}, {self.birth_day},\
             {self.position}, {self.salary}, {self.work_from})"


if __name__ == "__main__":
    Base.metadata.create_all(engine)