from database.db_handler import db

class Admission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program = db.Column(db.String(100))
    semester = db.Column(db.Integer)
    app_id = db.Column(db.Integer, db.ForeignKey('application.id'))