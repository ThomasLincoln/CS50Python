a = True
produtos = []
while a == True:
    try:
        item = input()
        quantidade = 0
        for produto in produtos:
            if item == produto["nome"]:
                quantidade = produto["quantidade"]
                produto["quantidade"] += 1
        if (quantidade <= 0):
            produto_aux = {
                "nome": item,
                "quantidade": 1,
            }
            produtos.extend([produto_aux])
        
    except EOFError:
        a = False

def get_key_nome(c):
  
      return c['nome']
  
produtos.sort(key=get_key_nome)

for produto in produtos:
    produto_aux = str(produto["nome"]).upper()
    print(produto["quantidade"], produto_aux)