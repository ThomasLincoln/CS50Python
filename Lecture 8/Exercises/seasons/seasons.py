from datetime import date
import sys
import re
import inflect

p = inflect.engine()

def main():
    data = input("Date of Birth: ")
    print(get_min(data))


    
def get_min(input):
    padrao = r"(\d{4})-(\d{2})-(\d{2})$"
    if search := re.search(padrao,input):
        input=list(search.groups())
    else:
        sys.exit('Invalid date')
    
    input_nasc = convert(input)

    hoje = date.today()

    aniversario = date(input_nasc[0], input_nasc[1], input_nasc[2])

    diferenca = aniversario - hoje

    numero_de_dias = -int(diferenca.days)

    minutos = numero_de_dias * 24 * 60
    frase = p.number_to_words(minutos)
    frase = frase.replace(' and','').capitalize()
    return frase + ' minutes'


def convert(dia):
    dia = list(map(int, dia))

    if dia[1] < 0 or dia[1] > 12:
        sys.exit('Invalid date')

    elif dia[2] < 0 or dia[2] > 31:
        sys.exit('Invalid date')

    return dia


if __name__ == "__main__":
    main()