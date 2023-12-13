from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase

from config import engine

class Base(DeclarativeBase):
    pass


class Auther(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)



def main():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()