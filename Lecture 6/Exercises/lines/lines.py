import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else: 
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            linhas = contar_linhas(sys.argv[1])
            print(linhas)

def contar_linhas(string):
    try:
        counter = 0
        with open(string, "r") as f:
            for line in f:
                if not(line.lstrip().startswith("#") or line.strip() == ""):
                    counter += 1
            return counter
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()