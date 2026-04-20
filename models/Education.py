class Education:
    def __init__(self, degree, institute, year):
        self.__degree = degree
        self.__inst = institute
        self.__year = year
    def display_info(self):
        print(
            "Degree:", self.__degree,
            "\nInstitute:", self.__inst,
            "\nYear:", self.__year
        )
