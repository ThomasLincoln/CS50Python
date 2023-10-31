name = input("Qual é o seu nome?\n")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Grifinória")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")
        