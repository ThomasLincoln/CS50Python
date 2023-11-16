import random 

flag = False
resposta_user = -1
nivel = -1

# Definindo o nível
while flag == False:
    try:
        nivel = int(input("Level: "))
    except: 
        pass

    if nivel >= 1:
        flag = True

resposta = random.randint(1, nivel)

while resposta_user != resposta:
    try:
        resposta_user = int(input("Guess: "))
        if resposta_user >= 1:
            if resposta_user < resposta:
                print("Too small!")
            elif resposta_user > resposta:
                print("Too large!")
            elif resposta_user == resposta:
                print("Just right!")

    except: 
        pass

