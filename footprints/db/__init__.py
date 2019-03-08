import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///' + os.path.join(os.path.dirname(__file__), 'db.sqlite3'))
Session = sessionmaker(engine)
session = Session()
Base = declarative_base()
