# Forma simples de inserir no txt
# name = input("Qual o Seu nome? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# Forma melhorada de inserir no txt
# name = input("Qual o Seu nome? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# 
# with open("names.txt", "r") as file:
    # for line in file:
        # print("Hello", line.rstrip())


# Forma para salvar e organizar os dados
# names = []

# with open("name.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names)
#     print(f"Hello,", name)

# Forma para organizar e printar os dados de forma otimizada
with open("names.txt", "r") as file:
    for line in sorted(file):
        print("Hello", line.rstrip())