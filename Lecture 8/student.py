class Student:
    def __init__(self, name, patronus, house):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "/"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name: 
            raise ValueError("Está faltando o nome")
        self._name = name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Casa inválida")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, patronus, house)

def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()

# ? Aqui a função sem usar objeto

# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house] # Se não retornar entre colchetes vai ser uma variável imutável
