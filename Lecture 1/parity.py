# Como fazer módulo?


def is_even(n):
    if n % 2 == 0: 
        return True
    else: 
        return False
    
def main():
    x = int(input("Qual o valor de X? "))
    if is_even(x):
        print("Par")
    else:
        print("Impar")

main()