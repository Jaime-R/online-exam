# coding=utf-8

from flask import Flask, jsonify, request

from src.entities.entity import engine, Base, session
from src.entities.exam import Exam, ExamSchema


# Creatin the Flask aplication
app = Flask(__name__)

#if needed, generate database Schema
Base.metadata.create_all(engine)

@app.route('/exams')
def get_exams():
	#fetching from the database
	#session = Session()
	#check for existing data
	exams_objects = session.query(Exam).all()

	#Transforming into JSON-serializable objects
	schema = ExamSchema(many=True)
	exams = schema.dump(exams_objects)

	#serializing as Json
	session.close()
	return jsonify(exams)



@app.route('/exams', methods=['POST'])
def add_exam():
	 # mount exam object
	posted_exam = ExamSchema(only=('title', 'description'))\
		.load(request.get_json())

	# Create Temporal ID
	exam = Exam(**posted_exam, created_by="HTTP post request")
	exam.id = 1234  # Temporal ID

	print("ID del objeto exam:",exam.id)
	# persist exam
	#session = Session()
	#session.add(exam)
	#session.commit()

	#fresh_exam = session.query(Exam).get(exam.id)
	#return created exam
	new_exam = ExamSchema().dump(exam)
	session.close()
	return jsonify(new_exam), 201
