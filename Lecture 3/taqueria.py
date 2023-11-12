cardapio = [
    {
        "nome": "Baja Taco",
        "preco": 4.25,
    },
    {
        "nome": "Burrito",
        "preco": 7.50,
    },
    {
        "nome": "Bowl",
        "preco": 8.50,
    },
    {
        "nome": "Nachos",
        "preco": 11.00,
    },
    {
        "nome": "Quesadilla",
        "preco": 8.50,
    },
    {
        "nome": "Super Burrito",
        "preco": 8.50,
    },
    {
        "nome": "Super Quesadilla",
        "preco": 9.50,
    },
    {
        "nome": "Taco",
        "preco":  3.00,
    },
    {
        "nome": "Tortilla Salad",
        "preco": 8.00,
    },
]

a = True
somatorio = 0
while a == True:
    try:    
        itemInput = input("Item: ")
        for item in cardapio:
            if itemInput == item["nome"]:
                somatorio = somatorio + item["preco"]
                print(f"Total: ${somatorio:.2f}")
                break
        if(itemInput == ""):
            a = False
    except EOFError: 
        a = False
        
        
