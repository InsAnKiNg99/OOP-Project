from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from database.db_handler import db

from models.Person import Person
from models.Student import Student
from models.Application import Application
from models.Education import Education
from models.Admission import Admission

from services.application_services import process_admission

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

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
    final_data = {
        **session.get('personal_data', {}),
        **session.get('education_data', {}),
        **request.form
    }
    process_admission(final_data)
    session.clear()
    return "<h1>Application Complete!</h1>"

@app.route('/students')
def view_students():
    all_students = Student.query.all()
    return render_template('students.html', students=all_students)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)