x = int(input("Qual o valor de X?\n"))
y = int(input("Qual o valor de Y?\n"))

if x < y:
    print("X é menor que Y")
elif x > y: 
    print("X é maior que Y")
elif x == y: 
    print("X é igual a Y")
    
# OR
if x < y or x > y:
    print("X é diferente de Y")
else: 
    print("X é igual a Y")
    
# Different
if x != y:
    print("X é diferente de Y")
else: 
    print("X é igual a Y")
