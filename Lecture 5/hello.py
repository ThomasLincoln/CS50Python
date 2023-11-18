def main():
    name = input("Qual é o seu nome? ")
    print(hello(name))    
    
def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()