def main():
    x = int(input("Qual o valor de X?"))
    print ("O quadrado de X é:", square(x))
    
def square(n):
    return n * n

if __name__ == "__main__":
    main()