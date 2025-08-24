# coding=utf-8

from sqlalchemy import  Column, String
from .entity import Entuty, Base

class Exam (Entity, Base)
	_tablename_ = 'exams'

	title = Column(String)
	description = Column(String)

	def _init_(self, title, description, created_by):
		Entity._init_(self, created_by)
		self.title = title
		self.description = description

