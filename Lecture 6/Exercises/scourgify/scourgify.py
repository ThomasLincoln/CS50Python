import sys
import csv


def main():
    tamanho = len(sys.argv)
    if tamanho > 3:
        sys.exit("Too many command-line arguments")
    if tamanho < 3:
        sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            limpar(sys.argv[1], sys.argv[2])


def limpar(before, after):
    try:
        with open(before) as before:
            reader = csv.DictReader(before)
            
            with open(after, "w") as after:
                writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for rows in reader:
                    nome, sobrenome = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow({"first": nome, "last": sobrenome, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {after}")


if __name__ == "__main__":
    main()