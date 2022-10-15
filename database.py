from lib2to3.pytree import Base
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker


engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/Carford')

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session