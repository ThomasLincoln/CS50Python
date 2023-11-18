def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if verify_size(s) == False:
       return False
    if two_letters(s) == False:
        return False
    if only_letter(s) == False:
        return False
    if number_in_middle(s) == True: 
        return False
    if first_number_is_zero(s) == True: 
        return False
    return True

def first_number_is_zero(s):
    for letra in s:
        if letra.isdecimal():
            if letra == "0":
                return True
            else:
                return False
        


def number_in_middle(s): 
    tamanho = len(s)

    if tamanho % 2 == 0:
        localizacao = int(tamanho/2 - 1)
        if s[localizacao].isdecimal() and s[localizacao - 1].isdecimal():
            return True
    else:
        if tamanho == 5:
            localizacao = round(tamanho/2)
        elif tamanho == 3: 
            localizacao = round(tamanho/2) - 1
        if s[localizacao].isdecimal():
            return True
    
    return False

def only_letter(s):
    return s.isalnum()
    
def verify_size(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    else: 
        return False
    
def two_letters(s):
    return s[0].isnumeric() == False and s[1].isnumeric() == False

if __name__ == "__main__":
    main()