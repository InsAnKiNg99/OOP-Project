import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, str(email)) is not None

def validate_phone(phone):
    phone_str = str(phone).strip()
    phone_cleaned = re.sub(r'[\s\-().+]', '', phone_str)
    return phone_cleaned.isdigit() and 7 <= len(phone_cleaned) <= 11

def validate_name(name):
    name_str = str(name).strip()
    return len(name_str) >= 2 and all(c.isalpha() or c.isspace() for c in name_str)

def validate_year(year):
    try:
        year_int = int(year)
        return 1900 <= year_int <= 2100
    except (ValueError, TypeError):
        return False

def validate_address(address):
    return len(str(address).strip()) >= 5

def validate_semester(semester):
    try:
        sem = int(semester)
        return sem in [1, 2]
    except (ValueError, TypeError):
        return False