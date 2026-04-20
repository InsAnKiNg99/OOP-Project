from Person import Person
class Student(Person):
    def __init__(self, stuId, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self._stuId = stuId
    def display_info(self):
        print(
            'Id:', self._stuId,
            '\nName:', self._name,
            '\nemail:', self._email,
            '\nphone:', self._phone,
            '\naddress:', self._address
        )
s1 = Student(1112081, "Muneer Hameed", "mhameedhameed90@gmail.com", "03302280608", "uot")
print(s1.display_info())