import sys
import os
import re

def verify_file():
    tamanho = len(sys.argv)
    try: 
        nome_arquivo = sys.argv[1]
        extensao_arquivo = os.path.splitext(nome_arquivo)[1]
        if extensao_arquivo != ".py":
            print("Not a Python file")
            sys.exit()
        if tamanho > 2:
            print("Too many command-line arguments")
            sys.exit()
    except:
        if tamanho < 2:
            print("Too few command-line arguments ")
            sys.exit()
    return nome_arquivo

def remover_espacos_ate_primeira_letra(string):
    for i in range(len(string)):
        if not string[i].isspace():
            return string[i:]
    return ""


def main():
    arquivo = verify_file()   
    count = 0
    try: 
        file = open(arquivo, "a")
    except: 
        print("File does not exist")
        sys.exit()

    with open(arquivo, "r") as file:
        for line in file:
            linha_sem_tabs = line.expandtabs(4)
            comeca = line.startswith("#")
            so_espaco = line.isspace()
            resposta = remover_espacos_ate_primeira_letra(line)
            comeca2 = resposta.startswith("#")
            if not comeca and not so_espaco and not comeca2:
                count += 1
    print(count)

main()