import sys
import csv

before = sys.argv[1]
after = sys.argv[2]

def verify_file():
    tamanho = len(sys.argv)
    try: 
        if tamanho > 3:
            print("Too many command-line arguments")
            sys.exit()
        with open(before, "r") as file:
            reader = csv.reader(file)
    except:
        if tamanho < 3:
            print("Too few command-line arguments ")
            sys.exit()
        print(f"Could not read {before}")

verify_file()

students = []

with open(before, "r") as file:
    reader = csv.DictReader(file)
    colunas = reader.fieldnames
    for row in reader:
        nome, sobrenome = row[colunas[0]].rstrip().split(", ")
        house = row[colunas[1]]
        # print(nome, sobrenome)
        student = {"first": nome, "last": sobrenome, "house": house}
        students.append(student)

with open(after, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        writer.writerow(student)
