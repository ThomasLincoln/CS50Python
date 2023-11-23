import csv
# # ? Aqui temos uma forma de salvar cada linha do csv em uma variavel
# with open("students.csv") as file: 
#     for line in file: 
#         row = line.rtstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")


# # ? Aqui temos uma forma de salvar cada linha do csv em uma variavel, porém, 
# # ? dessa vez salvando em variáveis especificas
# with open("students.csv") as file: 
#     for line in file: 
#         name, house = line.rtstrip().split(",")
#         print(f"{name} is in {house}")

# ? Aqui temos uma forma de ordenar os dados do csv usando uma função get_name
# students = []

# with open("students.csv") as file: 
#     for line in file: 
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key = get_name):
#     print(f"{student['name']} is in {student['house']}")


# ? Aqui temos uma forma de ordenadar os dados usando uma função lambda, como a 
# ? arrow function de js
# students = []
# with open("students.csv") as file: 
#     for line in file: 
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

# ? Agora usando funções do csv


# students = []
# with open("students.csv") as file: 
#     reader = csv.reader(file)
#     for name, house in reader:
#         students.append({"name": name, "home": house})

# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

# ? Inserir dados no csv

name = input("Qual o seu nome?")
house = input("Qual a sua casa?")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])
