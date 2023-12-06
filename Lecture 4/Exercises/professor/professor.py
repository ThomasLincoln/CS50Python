import random
import sys

def main():
    nivel = get_level()
    score = game(nivel) 
    print("Score: ", score)
    sys.exit()

def game(level):
    rodadas = 10
    pontuacao = 0
    while rodadas >= 1:
        x = generate_integer(level)
        y = generate_integer(level)
        resposta = rodada(x,y)
        if resposta == True:
            pontuacao += 1
        rodadas -= 1
    return pontuacao

def rodada(x,y):
    vidas = 3   
    while vidas >= 1:
        try:
            resposta = int(input(f" {x} + {y} = "))
            resultado = x + y
            if resultado == resposta:
                return True
            else:
                vidas -=1
                print("EEE")
        except (ValueError, NameError):
            vidas -=1
            print("EEE")
    print((f"{x} + {y} = {resultado}"))
    
def get_level():
    while True:
        try:
            n = input("Level: ")
            if n in ["1","2","3"]:
                break
        except ValueError:
            pass
    return int(n)


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
    return x

if __name__ == "__main__":
    main()
