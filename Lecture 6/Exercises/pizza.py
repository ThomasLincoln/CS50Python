import csv
import sys
from tabulate import tabulate

colunas = []
table = []
linha = []

def ler_arquivo(arquivo):
    with open(arquivo, "r") as file:
        reader = csv.DictReader(file)
        colunas = reader.fieldnames

        for row in reader:
            linha = []
            for coluna in colunas:
                linha.append(row[coluna])
            table.append(linha)

        return table, linha


if len(sys.argv) != 2:
    exit()

arquivo = sys.argv[1]

table, linha = ler_arquivo(arquivo)

print(tabulate(table, linha, tablefmt="outline"))
