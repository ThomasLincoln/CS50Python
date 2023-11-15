from random import choice, randint, shuffle
coin = choice(["Heads", "Tails"])
print(coin)

number = randint(1,10)
print(f"numero: {number}")

cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)
