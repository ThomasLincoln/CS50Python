def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # print(verify_size(s))
    if verify_size(s) == False:
        return False
    # print(two_letters(s))
    if two_letters(s) == False:
        return False
    # print(only_letter(s))
    if only_letter(s) == False:
        return False
    # print(number_in_middle(s))
    if number_in_middle(s) == True: 
        return False
    # print(first_number_is_zero(s))
    if first_number_is_zero(s) == True: 
        return False
    return True

def first_number_is_zero(s):
    for char in s:
        if char.isdigit():
            return char == "0"
    return False



def number_in_middle(s): 
    tamanho = len(s)

    if tamanho % 2 == 0:  # Se o tamanho for par
        meio = tamanho // 2
        if s[meio - 1].isdigit() and s[meio].isdigit():
            return True
    else:  # Se o tamanho for ímpar
        meio = tamanho // 2
        if s[meio].isdigit():
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
    
main()

