x = float(input("Qual o valor de X? "))
y = float(input("Qual o valor de Y? "))

z = round(x / y, 2)

print(z)

# * Resultado arredondado, vamos usar round para arredondar

def main():
    x = int(input("Qual o valor de X?"))
    print("X ao quadro é: ", square(x))
    

def square(n):
    return n * n

main()