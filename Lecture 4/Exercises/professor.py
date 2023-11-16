import random

def main():
    nivel = get_level()
    vidas = 3
    partidas = 10 
    pontuacao = 0

    while partidas :
       x = generate_integer(nivel)
       y = generate_integer(nivel)
    
       resultado = x + y
       acertou = False
       while vidas > 0 and acertou == False:
           resposta = int(input(f"{x} + {y} = "))
           if resposta != resultado:
               print("EEE")
               vidas -= 1
           else:
               acertou = True
               partidas -= 1
               pontuacao += 1

           if vidas < 1:
                partidas = 0
                break
    print(f"Score: {pontuacao}")

def get_level():
    # Descobrindo o nível   
    nivel = 0
    flag = False
    while flag == False :
        try:
            nivel = int(input("Level: "))
            print(nivel)
            if nivel == 1 or nivel == 2 or nivel == 3:
                flag = True
        except: 
            pass

    return nivel

def generate_integer(nivel):
    if nivel == 1:
        return random.randint(0, 9)
    elif nivel == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

main()
