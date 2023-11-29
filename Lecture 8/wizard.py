class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

class Student(Wizard):
    def __init__ (self, name, house):
        super().__init__(name)
        self._house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self._subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")