def rest():
    i = 0
    while i <= 2:
        print("Meow")
        i +=1
    print("--------------")

    for i in  range(3):
        print("Meow")

    print("--------------")    



def main():
    number = get_number()
    meow(number)
    
def get_number():
    n = int(input("Qual o valor de N? "))
    while (n < 0):
        n = int(input("Qual o valor de N? "))
    return n
    
def meow(n):
    for i in n:
        print("Meow")
        
main()