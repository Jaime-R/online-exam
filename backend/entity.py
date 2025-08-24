# coding=utf-8

from datetime import datetime
from sqlalchemy import create_egine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy-orm import sessionmaker

db_url = 'localhost:5432'
db_name = 'online-exam'
db_user = 'postgres'
db_password = 'ONLIN3-ex4m'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity():
	id = Column(Integer, primary_key=True)
	created_at = Column(DateTime)
	update_at = Column(DateTime)
	last_update_by = Column(String)

def _init_(Self, created_by):
	self-created_at = datetime.now()
	self.updated_at = datetime.now()
	self.last_updated_by = created by
