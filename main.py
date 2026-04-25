from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from database.db_handler import db
import logging
from logging.handlers import RotatingFileHandler
import os
import traceback

from models.Person import Person
from models.Student import Student
from models.Application import Application
from models.Education import Education
from models.Admission import Admission

from services.application_services import process_admission

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

log_dir = os.path.join(Config.BASE_DIR, 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

file_handler = RotatingFileHandler(
    os.path.join(log_dir, 'app.log'),
    maxBytes=10240,
    backupCount=10
)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

logging.getLogger('werkzeug').setLevel(logging.ERROR)
logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

@app.route('/')
def index():
    try:
        return render_template('personal.html')
    except Exception as e:
        app.logger.error(f"Error in index route: {str(e)}\n{traceback.format_exc()}")
        return render_template('error.html', 
                             message="An error occurred while loading the form",
                             error_code="ERR_INDEX"), 500

@app.route('/educational', methods=['POST'])
def educational():
    try:
        session['personal_data'] = request.form.to_dict()
        return render_template('educational.html')
    except Exception as e:
        app.logger.error(f"Error in educational route: {str(e)}\n{traceback.format_exc()}")
        return render_template('error.html', 
                             message="An error occurred while processing your personal information",
                             error_code="ERR_EDUCATIONAL"), 500

@app.route('/admission', methods=['POST'])
def admission():
    try:
        if 'personal_data' not in session:
            app.logger.warning("Educational route called without personal data in session")
            return render_template('error.html',
                                 message="Session expired or invalid flow. Please start over.",
                                 error_code="ERR_SESSION_EXPIRED"), 400
        
        session['education_data'] = request.form.to_dict()
        return render_template('admission.html')
    except Exception as e:
        app.logger.error(f"Error in admission route: {str(e)}\n{traceback.format_exc()}")
        return render_template('error.html',
                             message="An error occurred while processing your educational information",
                             error_code="ERR_ADMISSION"), 500

@app.route('/submit', methods=['POST'])
def submit():
    try:
        personal_data = session.get('personal_data', {})
        education_data = session.get('education_data', {})
        admission_data = request.form.to_dict()
        
        if not personal_data or not education_data:
            app.logger.warning("Submit route called without complete session data")
            return render_template('error.html',
                                 message="Session expired or invalid flow. Please start over.",
                                 error_code="ERR_INCOMPLETE_SESSION"), 400
        
        final_data = {**personal_data, **education_data, **admission_data}
        
        try:
            application = process_admission(final_data)
            session.clear()
            return render_template('success.html')
        except ValueError as ve:
            app.logger.warning(f"Validation error in submit: {str(ve)}")
            return render_template('error.html',
                                 message=f"Please check your input: {str(ve)}",
                                 error_code="ERR_VALIDATION"), 400
        except Exception as db_error:
            app.logger.error(f"Database error in submit: {str(db_error)}\n{traceback.format_exc()}")
            return render_template('error.html',
                                 message="An error occurred while saving your application. Please try again.",
                                 error_code="ERR_DATABASE"), 500
            
    except Exception as e:
        app.logger.error(f"Error in submit route: {str(e)}\n{traceback.format_exc()}")
        return render_template('error.html',
                             message="An unexpected error occurred while processing your application",
                             error_code="ERR_SUBMIT"), 500

@app.route('/students')
def view_students():
    try:
        try:
            all_students = Student.query.all()
            if not all_students:
                app.logger.info("No students found in database")
            return render_template('students.html', students=all_students)
        except Exception as db_error:
            app.logger.error(f"Database error while fetching students: {str(db_error)}\n{traceback.format_exc()}")
            return render_template('students.html', students=[])
    except Exception as e:
        app.logger.error(f"Error in view_students route: {str(e)}\n{traceback.format_exc()}")
        return render_template('error.html',
                             message="An error occurred while retrieving student records",
                             error_code="ERR_STUDENTS_VIEW"), 500

@app.errorhandler(404)
def not_found_error(error):
    app.logger.warning(f"404 Error: {request.url}")
    return render_template('error.html',
                         message="The page you're looking for doesn't exist.",
                         error_code="ERR_404"), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    app.logger.error(f"500 Error: {str(error)}\n{traceback.format_exc()}")
    return render_template('error.html',
                         message="An internal server error occurred. Please try again later.",
                         error_code="ERR_500"), 500

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            app.logger.info("Database tables created successfully")
        except Exception as e:
            app.logger.error(f"Error creating database tables: {str(e)}\n{traceback.format_exc()}")
    
    app.run(debug=False, use_reloader=False)