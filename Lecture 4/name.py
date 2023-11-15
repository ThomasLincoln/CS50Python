import sys

# Verificação de Erros
if len(sys.argv) < 2:
    sys.exit("Too few arguments") 

# Print the name
for arg in sys.argv[1:]:
    print(f"Olá, meu nome é: {arg}")