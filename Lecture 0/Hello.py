# Ask to user their name
# name = input("What's your name? ")

# * Say hello to user, versão simplória
# print ("Hello, ", end="")
# print (name, end="")
# print (" my dear \"friend\"")

# * Podemos formatar de outra forma também: 

# print(f"Hello, {name}")

# ! String Methods

# * Nós conseguimos remover os espaços dos lados usado essa função:

# name = name.strip()
# print(f"Hello, {name}")

# * Podemos capitalizar a string

# name = name.capitalize()
# print(f"Hello, {name}")

# * Também podemos capitalizar todas as palavras

# name = name.title()
# print(f"Hello, {name}")

# * Também, podemos fazer tudo junto: 

# name = name.strip().title()
# print(f"Hello, {name}")


# * Podemos inclusive, juntar tudo em um: 


def hello(to="world"):
    print("Hello,", to)

def main():
    hello()
    name2 = input("Digite seu nome: ").strip().title()
    hello(name2)
    
main()