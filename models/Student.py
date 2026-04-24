from models.Person import Person
from database.db_handler import db

class Student(Person):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    student_id = db.Column(db.String(20), unique=True)
    applications = db.relationship('Application', backref='student', lazy=True, cascade='all, delete-orphan')
    
    def __init__(self, name=None, email=None, phone=None, address=None):
        super().__init__(name, email, phone, address)
    
    def __repr__(self):
        return f'<Student {self.student_id}>'
    
    def get_info(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Email: {self.email}"
    
    def add_application(self, application):
        if application not in self.applications:
            self.applications.append(application)
    
    def get_applications_count(self):
        return len(self.applications)
    
    def get_application_status(self):
        return {app.id: app.status for app in self.applications}