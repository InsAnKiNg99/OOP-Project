from database.db_handler import db
from models.Student import Student
from models.Application import Application
from models.Admission import Admission
from models.Education import Education

def process_admission(data):
    student = Student(
        name=data.get('name'),
        email=data.get('email'),
        phone=data.get('phone'),
        address=data.get('address')
    )
    db.session.add(student)
    db.session.flush()
    
    student.student_id = f"STU-{student.id:04d}"
    db.session.flush()

    application = Application(status="Pending")
    application.student_id = student.id
    db.session.add(application)
    db.session.flush()

    admission = Admission(
        program=data.get('program'),
        semester=data.get('semester')
    )
    admission.app_id = application.id
    db.session.add(admission)
    
    education = Education(
        degree=data.get('degree'),
        institute=data.get('institute'),
        year=data.get('year')
    )
    education.app_id = application.id
    db.session.add(education)
    
    db.session.commit()
    return application