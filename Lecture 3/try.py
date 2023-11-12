def main():
    x = get_int()
    print(f"O valor de x é: {x}")
    
def get_int():
    while True: 
        try:
            return int(input("Qual o valor de X? "))
        except:
            pass
            
            
main()