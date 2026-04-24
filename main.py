from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from database.db_handler import db
import logging
from logging.handlers import RotatingFileHandler
import os

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

logging.getLogger('werkzeug').setLevel(logging.ERROR)
logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

@app.route('/')
def index():
    return render_template('personal.html')

@app.route('/educational', methods=['POST'])
def educational():
    session['personal_data'] = request.form
    return render_template('educational.html')

@app.route('/admission', methods=['POST'])
def admission():
    session['education_data'] = request.form
    return render_template('admission.html')

@app.route('/submit', methods=['POST'])
def submit():
    personal_data = session.get('personal_data', {})
    education_data = session.get('education_data', {})
    admission_data = request.form
    
    final_data = {**personal_data, **education_data, **admission_data}
    process_admission(final_data)
    session.clear()
    
    return render_template('success.html')

@app.route('/students')
def view_students():
    all_students = Student.query.all()
    return render_template('students.html', students=all_students)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, use_reloader=False)