# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .entity import Entity, Base


class Exam(Base, Entity):
	__tablename__ = 'exams'

	title = Column(String)
	description = Column(String)

	def __init__(self, title, description, created_by):
		Entity.__init__(self, created_by)
		self.title = title
		self.description = description

class ExamSchema(Schema):
	id = fields.Integer()
	title = fields.Str()
	description = fields.Str()
	created_at = fields.DateTime()
	updated_at = fields.DateTime()
	last_updated_by = fields.Str()


