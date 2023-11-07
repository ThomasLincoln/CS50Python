variavel = input("Input: ")
vrvl = ""
for letra in variavel:
    if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
        vrvl += letra
        
print(f"Output: {vrvl}")