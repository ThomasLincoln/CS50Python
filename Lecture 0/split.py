name = input("Qual o seu nome? \n").strip().title()

# * Agora, vamos aprender um pouco sobre dividir a string

first, last = name.split(" ")

print(f"Hello {last}, {first}")