import random

def main():
    nivel = get_level()
    resposta = generate_integer(nivel)
    play_game(resposta)

def get_level():
    flag = False
    nivel = -1

    while not flag:
        try:
            nivel = int(input("Level: "))
        except ValueError:
            pass

        if 1 <= nivel <= 3 and nivel > 0:
            flag = True

    return nivel

def generate_integer(level):
    return random.randint(1, level)

def play_game(resposta):
    resposta_user = -1

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

        except ValueError:
            pass

if __name__ == "__main__":
    main()
