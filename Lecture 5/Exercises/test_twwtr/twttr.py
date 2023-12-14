def main():
    variavel = input("Input: ")
    response = shorten(variavel)
    print(response)

def shorten(word):
    vrvl = ""
    word = word.lower()
    for letra in word:
        if (letra != "a") and letra != "e" and letra != "i" and letra != "o" and letra != "u":
            vrvl += letra
    return vrvl

if __name__ == "__main__":
    main()