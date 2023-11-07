variavel = input("camelCase: ")
variavel_snake_case = ""
for letra in variavel:
    if(letra.isupper()):
        variavel_snake_case += "_"
        variavel_snake_case += letra.lower()
    else: 
        variavel_snake_case += letra
        
print(f"snake_case: {variavel_snake_case}")