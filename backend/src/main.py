# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.exam import Exam

# generate database Schema
Base.metadata.create_all(engine)

# Start session
session = Session()


#check for existing data
exams = session.query(Exam).all()

if len(exams) == 0:
	# create a persist mock exam
	python_exam = Exam("SQLAlchemy Exam","Test your Knowledge about SQLalchemy.","script")
	session.add(python_exam)
	session.commit()
	session.close()

	# reload exams
	exams = session.query(Exam).all()

# show existing exams
print('### Exams:')
for exam in exams:
	print(f'({exam.id}) {exam.title} - {exam.description}')

