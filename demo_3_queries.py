from sqlalchemy import select
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.baked import Result
from sqlalchemy.orm import DeclarativeBase, Session

from config import engine

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, " f"user_name={self.username!r}, email={self.email!r})")


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(
        username=username,
        email=email,
    )
    print(user)
    session.add(user)
    session.commit()
    print("сохранили user")
    print("user details:", user)

def get_user_by_id(
    session: Session,
    user_id: int,
) -> User:
    """
    Frome cache
    :param session:
    :param user_id:
    :return:
    """
    user = session.get(User, user_id)
    print(user)
    return user

def find_user_by_id(
    session: Session,
    user_id: int,
):
    stmt = select(User).where(User_id == user_id)
    Result = session.execute(stmt)
    user = result.scalaro_one_or_none()

def main():
    # Base.metadata.drop_all(bind=engine) --- что бы удалять таблицы
    Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        #create_user(session, username="john")
        #create_user(session, username="sam")
        #create_user(session, username="bob")
        #create_user(session, username="nick")
        get_user_by_id(session, user_id=5)
        #get_user_by_id(session, user_id=2)
        #get_user_by_id(session, user_id=1)


if __name__ == "__main__":
    main()