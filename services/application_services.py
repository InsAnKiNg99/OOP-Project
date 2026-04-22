from database.db_handler import db
from models.Student import Student
from models.Application import Application
from models.Admission import Admission

def process_admission(data):
    student = Student(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        address=data.get('address'),
        stu_id_attr=data.get('stuId')
    )
    db.session.add(student)
    db.session.flush()

    app = Application(student_id=student.id)
    db.session.add(app)
    db.session.flush()

    admission = Admission(
        program=data['program'],
        semester=data['semester'],
        app_id=app.id
    )
    db.session.add(admission)
    db.session.commit()
    return app