import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"([a-zA-Z0-9]*)(?::)?([a-zA-Z0-9]*)? (\w*) to ([a-zA-Z0-9]*)(?::)?([a-zA-Z0-9]*)? (\w*)"
    try:
        matches = re.search(pattern, s)
        if not matches:
            raise ValueError("Formato inválido ou tempo inválido")
    except ValueError as e:
        print("Erro:", e) 

    if matches:
        horaComeco = int(matches.group(1))
        periodoComeco = matches.group(3)
        
        horaFim = int(matches.group(4))
        periodoFim = matches.group(6)
        
        if(matches.group(2)):
            minutoComeco = int(matches.group(2))
        else:
            minutoComeco = 0

        if(matches.group(5)):
            minutoFim = int(matches.group(5))
        else:
            minutoFim = 0
    else: 
        raise ValueError("Formato Inválido")

    if not(minutoComeco >= 0 and minutoComeco < 60): 
        raise ValueError("Minutos inválidos")
        sys.exit()
    if not(minutoFim >= 0 and minutoFim < 60): 
        raise ValueError("Minutos inválidos")
        sys.exit()

    # Convertendo minutos nulos
    if minutoComeco == 0:
        minutoComeco = f"00"
    if minutoFim == 0:
        minutoFim = f"00"


    if(periodoComeco == "PM"):
        horaComeco += 12
    if(periodoFim == "PM"):
        horaFim += 12
    if horaComeco < 10:
        horaComeco = f"0{horaComeco}"
    if horaFim< 10:
        horaFim = f"0{horaFim}"
    
    if periodoComeco == "AM" and horaComeco == 12:
        horaComeco = "00"
    if periodoFim == "PM" and horaFim == 24:
        horaFim = 12
    
    return f"{horaComeco}:{minutoComeco} to {horaFim}:{minutoFim}"
        
# 9 AM to 5 PM



if __name__ == "__main__":
    main()