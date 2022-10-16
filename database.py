import dotenv
import os
from lib2to3.pytree import Base
import sqlalchemy
from sqlalchemy import text
from sqlalchemy.orm import declarative_base, sessionmaker

dotenv.load_dotenv(dotenv.find_dotenv())

engine = sqlalchemy.create_engine('postgresql://{}:{}@{}:{}/{}'.format(os.getenv("USUARIO"),os.getenv("SENHA"), os.getenv("HOST"), os.getenv("PORT"), os.getenv("DB_NAME")))

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


for i in range(1,1):
    conn = engine.connect()
    conn.execute(text("INSERT INTO cores VALUES (1, 'Amarelo')"))
    conn.execute(text("INSERT INTO cores VALUES (2, 'Azul')"))
    conn.execute(text("INSERT INTO cores VALUES (3, 'Cinza')"))
    conn.execute(text("INSERT INTO modelos VALUES ('Hacth')"))
    conn.execute(text("INSERT INTO modelos VALUES ('Sedan')"))
    conn.execute(text("INSERT INTO modelos VALUES ('Conversível')"))
    conn.close()