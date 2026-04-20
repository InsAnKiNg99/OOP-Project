class Person:
    def __init__(self, name, email, phone, address):
        self._name = name
        self._email = email
        self._phone = phone
        self._address = address
    def display_info(self):
        print(
            'Name:', self._name,
            '\nemail:', self._email,
            '\nphone:', self._phone,
            '\naddress:', self._address
        )
        
p = Person("Muneer Hameed", "mhameedhameed90@gmail.com", "03302280608", "uot")
