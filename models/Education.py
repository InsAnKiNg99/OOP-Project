from database.db_handler import db

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(100))
    institute = db.Column(db.String(100))
    year = db.Column(db.Integer)
    app_id = db.Column(db.Integer, db.ForeignKey('application.id'))