from database.db_handler import db

class Person(db.Model):
    __abstract__ = True
    
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.Integer)
    address = db.Column(db.String(200))
    
    def __init__(self, name=None, email=None, phone=None, address=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    
    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}"
    
    def get_contact(self):
        return f"Phone: {self.phone}, Address: {self.address}"