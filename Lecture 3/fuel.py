def main():
    a = True
    while a == True:
        entrada = input("Fraction: ")
        try:
            x = int(entrada[0])  
            tamanho = len(entrada) - 1
            y = int(entrada[tamanho])  
            
            
            if x < y:
                a = False
            else:
                pass
            
            resultado = x/y
        except (ValueError, ZeroDivisionError):
            pass
    porcentagem = resultado * 100
    print(f"{porcentagem:.0f}%")
main()