class Student:
    def __init__(self, name, patronus, house=None):
        if not name: 
            raise ValueError("Está faltando o nome")
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

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, patronus, house)
        

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
