cardapio = [
    {
        "nome": "baja taco",
        "preco": 4.25,
    },
    {
        "nome": "burrito",
        "preco": 7.50,
    },
    {
        "nome": "bowl",
        "preco": 8.50,
    },
    {
        "nome": "nachos",
        "preco": 11.00,
    },
    {
        "nome": "quesadilla",
        "preco": 8.50,
    },
    {
        "nome": "super burrito",
        "preco": 8.50,
    },
    {
        "nome": "super quesadilla",
        "preco": 9.50,
    },
    {
        "nome": "taco",
        "preco":  3.00,
    },
    {
        "nome": "tortilla salad",
        "preco": 8.00,
    },
]

a = True
somatorio = 0
while a == True:
    try:    
        itemInput = input("Item: ").lower()
        for item in cardapio:
            if itemInput == item["nome"]:
                somatorio = somatorio + item["preco"]
                print(f"Total: ${somatorio:.2f}")
                break
        if(itemInput == ""):
            a = False
    except EOFError: 
        a = False
        
        
