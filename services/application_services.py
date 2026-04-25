from database.db_handler import db
from models.Student import Student
from models.Application import Application
from models.Admission import Admission
from models.Education import Education
from utilities.validators import (validate_email, validate_phone, validate_name, 
                                   validate_year, validate_address, validate_semester)
import logging

logger = logging.getLogger(__name__)

def validate_admission_data(data):
    """Validate all admission data before processing"""
    errors = []
    
    if not validate_name(data.get('name')):
        errors.append("Invalid name format")
    
    if not validate_email(data.get('email')):
        errors.append("Invalid email format")
    
    if not validate_phone(data.get('phone')):
        errors.append("Invalid phone number format")
    
    if not validate_address(data.get('address')):
        errors.append("Address must be at least 5 characters")
    
    if not data.get('degree'):
        errors.append("Degree is required")
    
    if not data.get('institute'):
        errors.append("Institute is required")
    
    if not validate_year(data.get('year')):
        errors.append("Invalid graduation year")
    
    if not data.get('program'):
        errors.append("Program selection is required")
    
    if not validate_semester(data.get('semester')):
        errors.append("Invalid semester selection")
    
    return errors

def process_admission(data):
    """Process admission with comprehensive error handling"""
    try:
        validation_errors = validate_admission_data(data)
        if validation_errors:
            logger.warning(f"Validation errors: {validation_errors}")
            raise ValueError("Validation failed: " + "; ".join(validation_errors))
        
        student = Student(
            name=str(data.get('name', '')).strip(),
            email=str(data.get('email', '')).strip().lower(),
            phone=str(data.get('phone', '')).strip(),
            address=str(data.get('address', '')).strip()
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
            program=str(data.get('program', '')).strip(),
            semester=int(data.get('semester', 1))
        )
        admission.app_id = application.id
        db.session.add(admission)
        
        education = Education(
            degree=str(data.get('degree', '')).strip(),
            institute=str(data.get('institute', '')).strip(),
            year=int(data.get('year', 2023))
        )
        education.app_id = application.id
        db.session.add(education)
        
        db.session.commit()
        logger.info(f"Admission processed successfully for student {student.student_id}")
        return application
        
    except ValueError as ve:
        db.session.rollback()
        logger.error(f"Validation error: {str(ve)}")
        raise ve
    except Exception as e:
        db.session.rollback()
        logger.error(f"Unexpected error in process_admission: {str(e)}")
        raise Exception(f"Failed to process admission: {str(e)}")