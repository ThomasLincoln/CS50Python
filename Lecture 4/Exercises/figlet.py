from random import choice
from sys import argv
from pyfiglet import Figlet, sys

figlet = Figlet()
fontes = figlet.getFonts()

if len(sys.argv) < 2: 
    # Escolhendo e setando a fonte
    fonte = choice(fontes)
    figlet.setFont(font = fonte)
    
    # Lendo e Printando o resultado
    texto = input("Input: ")
    print("Output: ")
    print(figlet.renderText(texto))
else:
    # Verificando se inseriu valores aceitaveis
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        contem = (argv[2] in fontes)
        if contem != True:
            sys.exit("Invalid usage")

        # Definindo a fonte
        fonte = sys.argv[2]
        figlet.setFont(font = fonte)
    
        # Lendo e Printando resultado
        texto = input("Input: ")
        print("Output: ")
        print(figlet.renderText((texto)))
    else: 
        sys.exit("Invalid usage")
