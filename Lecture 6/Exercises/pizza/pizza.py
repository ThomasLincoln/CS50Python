import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            print(tabelar(sys.argv[1]))

def tabelar(arquivo):
    try:
        with open(arquivo) as f:
            reader = csv.reader(f)
            table = tabulate(reader, headers ="firstrow", tablefmt="grid")
            return table
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()