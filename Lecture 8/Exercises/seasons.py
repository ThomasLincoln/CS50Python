from datetime import datetime
import sys
import re
import inflect

p = inflect.engine()

def main():
    ...
    nascData = get_input()
    data_atual = datetime.now()
    data_atual.replace(hour=0, minute=0, second=0, microsecond=0)
    nascData.replace(hour=0, minute=0, second=0, microsecond=0)
    
    print(data_atual)
    
    diferenca = data_atual - nascData
    minutos = diferenca.total_seconds() / 60
    resposta = p.number_to_words(minutos).capitalize()
    
    print(f"{resposta} minutes")

    
def verifica(data):
    # Filtrar erros no input
    padrao = r"\d{4}-\d{2}-\d{2}"
    if re.match(padrao, data):
        return True
    else:
        sys.exit("Invalid date")


def get_input():
    data = input("Date of Birth: ")
    resultado = verifica(data)
    return datetime.fromisoformat(data)
    

...



if __name__ == "__main__":
    main()