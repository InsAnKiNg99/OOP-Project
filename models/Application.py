from database.db_handler import db
from datetime import datetime

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="Pending")
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    education_records = db.relationship('Education', backref='application', lazy=True)
    admission_details = db.relationship('Admission', backref='application', uselist=False)