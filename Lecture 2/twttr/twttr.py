variavel = input("Input: ")
vrvl = ""
for letra in variavel:
    if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u" and letra != "O" and letra != "A" and letra != "E" and letra != "I" and letra != "U":
        vrvl += letra
        
print(f"Output: {vrvl}")