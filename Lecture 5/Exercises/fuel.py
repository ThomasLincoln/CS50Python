def main():
    values = leitura()
    gauge_value = gauge(values[2])
    print(gauge_value)
    
def leitura():
    flag = False
    while flag == False:
        entrada = input("Fraction: ")
        try: 
            values = convert(entrada)
            if values[0] < values[1]:
                flag = True
        except (ValueError, ZeroDivisionError):
            raise(ZeroDivisionError)
    return values

def convert(fraction):
    x = int(fraction[0])  
    tamanho = len(fraction) - 1
    y = int(fraction[tamanho])  
    z = (x / y) 
    return [x, y, z]


def gauge(percentage):
    print(percentage)
    if percentage < 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage * 100:.0f}%"

if __name__ == "__main__":
    main()