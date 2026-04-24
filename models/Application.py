from database.db_handler import db
from datetime import datetime

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="Pending")
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    education_records = db.relationship('Education', backref='application', lazy=True, cascade='all, delete-orphan')
    admission_details = db.relationship('Admission', backref='application', uselist=False, cascade='all, delete-orphan')
    
    def __init__(self, status="Pending"):
        self.date = datetime.utcnow()
        self.status = status
    
    def add_education_record(self, education):
        if education not in self.education_records:
            self.education_records.append(education)
    
    def set_admission_details(self, admission):
        self.admission_details = admission
    
    def get_application_summary(self):
        education_count = len(self.education_records)
        has_admission = self.admission_details is not None
        return f"Application ID: {self.id}, Status: {self.status}, Date: {self.date}, Education Records: {education_count}, Admission Details: {has_admission}"
    
    def update_status(self, new_status):
        self.status = new_status
        return f"Application status updated to: {self.status}"