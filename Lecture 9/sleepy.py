def main():
    n = int(input("Quantas ovelhas? "))
    for s in sheep(n):
        print(s)
        
def sheep(n):
    """
    retorna ovelhas
    """
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()