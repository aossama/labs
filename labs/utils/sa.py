import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class Database(object):
    def __init__(self):
        pass

    @classmethod
    def setup(cls):
        Base.metadata.create_all(cls.get_engine())

    # FIXME: This method obviously needs to take a proper database URL
    @classmethod
    def get_engine(cls):
        return create_engine(
            'sqlite:////tmp/labs.sqlite3',
            echo=False
        )

    @classmethod
    def get_session(cls):
        session = sessionmaker(bind=cls.get_engine())

        return session()


class BaseModel(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'

    def __init__(self):
        pass

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(255))

    # Resource ID
    rid = Column(String(10))

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    deleted_at = Column(DateTime)
    deleted = Column(Boolean, default=False)

    def save(self, session):
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


Base = declarative_base(cls=BaseModel)


class Lab(Base, BaseModel):
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    published = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return "<Lab %(id)d %(name)s %(uuid)s>" % {
            'id': self.id,
            'uuid': self.uuid,
            'name': self.name
        }
