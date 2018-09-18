import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///%s' % os.path.join(os.path.dirname(__file__), 'storage.sqlite3'))
Base = declarative_base()
Session = sessionmaker(engine)
session = Session()
