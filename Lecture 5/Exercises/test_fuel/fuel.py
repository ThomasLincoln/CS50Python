def main():
    fracao = input("Fraction: ")  
    porcentagem = convert(fracao)
    print(gauge(porcentagem))
    
def convert(combustivel):
    # * Tentar separar os valores
    x, y = combustivel.split("/")
    # * Converter em inteiros
    numerador = int(x)
    denominador = int(y)
    if numerador/denominador > 1:
        raise ValueError
    elif denominador == 0:
        raise ZeroDivisionError
    return int(numerador/denominador * 100)
    
def gauge(porcentagem):
    try:
        if 0 <= porcentagem <= 1:
            return "E"
        elif 99<= porcentagem <= 100:
            return "F"
        elif 1 < porcentagem < 99:
            return f"{porcentagem}%"
        else:
            raise TypeError
    except TypeError:
        pass
        
if __name__ == "__main__":
    main()