def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not verify_size(s):
       return False
    if not two_letters(s):
        return False
    if not only_letter(s):
        return False
    if number_in_middle(s):
        return False
    if first_number_is_zero(s):
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
    found_number = False

    for char in s:
        if found_number:
            if char.isalpha():
                return True
        elif char.isdigit():
            found_number = True

    return False



def only_letter(s):
    return s.isalnum()
    
def verify_size(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    else: 
        return False
    
def two_letters(s):
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    return True

if __name__ == "__main__":
    main()