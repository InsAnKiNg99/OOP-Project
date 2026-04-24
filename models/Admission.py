from database.db_handler import db

class Admission(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    program = db.Column(db.String(100))
    semester = db.Column(db.Integer)
    app_id = db.Column(db.Integer, db.ForeignKey('application.id'))
    
    def __init__(self, program=None, semester=None):
        self.program = program
        self.semester = semester
    
    def get_admission_info(self):
        return f"Program: {self.program}, Semester: {self.semester}"