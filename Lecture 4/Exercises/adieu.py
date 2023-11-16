import inflect

p = inflect.engine()

lista_de_nomes = []
flag = False

while flag == False:
    try: 
        nome = input("Name: ")
        lista_de_nomes.append(nome)
    except EOFError:
        flag = True
    
# Juntando os nomes
nomes = p.join(lista_de_nomes)
print(f"Adieu, adieu, to {nomes}")
