# UOT Admission Portal - Web Application

A full-fledged Flask web application for managing student admissions with comprehensive error handling and validation.

## Features

✅ Multi-step admission form (Personal → Educational → Admission)
✅ SQLite database with OOP design patterns
✅ Comprehensive input validation with error messages
✅ Robust error handling with logging
✅ View all applications
✅ Responsive glass-morphism UI
✅ Session management
✅ Database integrity with foreign keys

## Project Structure

```
├── main.py
├── config.py
├── requirements.txt
├── database/
│   ├── __init__.py
│   ├── db_handler.py
│   └── SQLite.db
├── models/
│   ├── __init__.py
│   ├── Person.py
│   ├── Student.py
│   ├── Application.py
│   ├── Education.py
│   └── Admission.py
├── services/
│   ├── __init__.py
│   └── application_services.py
├── utilities/
│   ├── __init__.py
│   └── validators.py
├── inputs/
│   ├── __init__.py
│   ├── personal.py
│   ├── educational.py
│   └── admission.py
├── templates/
│   ├── Base.html
│   ├── personal.html
│   ├── educational.html
│   ├── admission.html
│   ├── success.html
│   ├── students.html
│   └── error.html
├── static/
│   └── style.css
└── logs/
    └── app.log
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to project directory:**
   ```bash
   cd "h:\Muneer Hameed\OOP-Project"
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Method 1: Direct Python Execution
```bash
python main.py
```

### Method 2: Using Flask CLI
```bash
flask run
```

The application will start at `http://localhost:5000`

## Using the Application

1. **Submit an Application:**
   - Start at the home page (`/`)
   - Fill in personal information
   - Click "Continue to Next Step"
   - Fill in educational background
   - Click "Continue to Next Step"
   - Fill in admission details
   - Click "Submit Application"
   - View success page with working buttons

2. **View Submitted Applications:**
   - Click "View All Applications" on success page
   - Or navigate to `/students`

3. **Reset and Submit Another:**
   - Click "Submit Another Application" on success page
   - Or navigate to `/` to start fresh

## Validation Features

The application validates:
- **Email:** Valid email format (user@domain.com)
- **Phone:** 7-15 digit numbers with optional formatting
- **Name:** 2+ characters, alphabetic only
- **Year:** Valid graduation year (1900-2100)
- **Address:** Minimum 5 characters
- **Semester:** Valid selection (Fall or Spring)

## Error Handling

All routes include:
- ✅ Try-catch blocks
- ✅ Input validation
- ✅ Session state verification
- ✅ Database error handling
- ✅ Comprehensive logging
- ✅ User-friendly error pages

## Logging

Application logs are saved to `logs/app.log` with:
- Timestamp
- Log level (INFO, WARNING, ERROR)
- Message
- File and line number
- Log rotation (10 backup files, 10KB each)

## Bug Fixes Applied

1. **Success Page Buttons** - Centered and properly positioned (was `margin-left: 122%`)
2. **Phone Number Type** - Changed from Integer to String to support formatting
3. **Students Template** - Fixed undefined attribute `stu_id_attr` to `student_id`
4. **Data Validation** - Added comprehensive validators for all fields
5. **Error Handling** - Added try-catch blocks to all routes
6. **Database Integrity** - Added rollback on errors
7. **Session Management** - Validates session data before processing

## Development Notes

### Adding New Routes
```python
@app.route('/new-route', methods=['GET', 'POST'])
def new_route():
    try:
        # Your code here
        return render_template('template.html')
    except Exception as e:
        app.logger.error(f"Error in new_route: {str(e)}\n{traceback.format_exc()}")
        return render_template('error.html', 
                             message="Error message",
                             error_code="ERR_CODE"), 500
```

### Adding New Validators
1. Add function to `utilities/validators.py`
2. Import in `services/application_services.py`
3. Use in `validate_admission_data()` function

## Database

The application uses SQLite with the following tables:
- **student** - Student personal information
- **application** - Application records
- **education** - Educational background
- **admission** - Admission details

All related records are cascaded on delete for data integrity.

## Troubleshooting

### Issue: "Database is locked"
- Close all instances of the application
- Delete `database/SQLite.db`
- Restart the application

### Issue: "No module named..."
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Activate the virtual environment

### Issue: "Port 5000 already in use"
```bash
python main.py --port 5001
```

### Issue: "Cannot find logs directory"
The application auto-creates the logs folder on startup.

## License

Educational Project - UOT Admission System

## Support

For issues or questions, check the application logs at `logs/app.log` for detailed error information.
