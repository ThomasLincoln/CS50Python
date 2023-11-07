price = 50

while(price > 0):
    print(f"Amount Due: {price}")
    insercao = int(input("Inser Coin: "))
    if insercao == 5 or insercao == 10 or insercao == 25:
        price -= insercao
    
print(f"Change Owed: {price * -1}")    

    