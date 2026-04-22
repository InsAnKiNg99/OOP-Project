from models.Person import Person
from database.db_handler import db

class Student(Person):
    id = db.Column(db.Integer, primary_key=True)
    stu_id_attr = db.Column(db.String(20), unique=True)
    applications = db.relationship('Application', backref='student', lazy=True)

    def get_info(self):
        return f"Student ID: {self.stu_id_attr}, Name: {self.name}, Email: {self.email}"