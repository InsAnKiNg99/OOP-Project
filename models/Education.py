from database.db_handler import db

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    degree = db.Column(db.String(100))
    institute = db.Column(db.String(100))
    year = db.Column(db.Integer)
    app_id = db.Column(db.Integer, db.ForeignKey('application.id'))
    
    def __init__(self, degree=None, institute=None, year=None):
        self.degree = degree
        self.institute = institute
        self.year = year
    
    def get_education_info(self):
        return f"Degree: {self.degree}, Institute: {self.institute}, Year: {self.year}"