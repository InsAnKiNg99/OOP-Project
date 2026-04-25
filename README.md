# Student Admission Management System

A Flask-based web application for managing student admissions. Handles personal information, educational background, and application processing.

## Requirements

- Flask 3.0.0
- Flask-SQLAlchemy 3.1.1
- SQLAlchemy 2.0.23
- Python 3.7+

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

The application will start on `http://localhost:5000`

## Project Structure

- `models/` - Data models for Person, Student, Application, Education, and Admission
- `services/` - Business logic for processing admissions
- `database/` - Database handler and SQLite configuration
- `templates/` - HTML templates for web interface
- `static/` - CSS styles
- `inputs/` - Input validation and processing
- `utilities/` - Validator functions
- `logs/` - Application logs

## Usage

The application provides forms for:
- Personal information entry
- Educational background
- Admission application processing

All submissions are validated and stored in SQLite database.
