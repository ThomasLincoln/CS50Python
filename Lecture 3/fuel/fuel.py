def main():
    a = True
    while a == True:
        entrada = input("Fraction: ")
        try:
            numerador, denominador = entrada.split("/")
            x = int(numerador)
            y = int(denominador)
            
            resultado = x/y
            
            if x <= y and y != 0:
                a = False
            else: 
                pass
            
        except (ValueError, ZeroDivisionError):
            pass
    
    porcentagem = resultado * 100
    if porcentagem <= 1:
        print("E")
    elif porcentagem >= 99:
        print("F")
    else: 
        print(f"{porcentagem:.0f}%")
main()