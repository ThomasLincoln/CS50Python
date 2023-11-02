response = input("Expression: ")

partes = response.rsplit(" ", 3)

match partes[1]:
    case "+":
        result = float(partes[0]) + float(partes[2])
    case "/":
        result = float(partes[0]) / float(partes[2])
    case "*":
        result = float(partes[0]) * float(partes[2])
    case "-":
        result = float(partes[0]) - float(partes[2])

print(result)
