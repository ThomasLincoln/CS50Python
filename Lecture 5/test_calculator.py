from calculator import square

def main():
    test_square()

def test_square():
    try: 
        assert square(2) == 4
    except AssertionError:
        print("A raiz de 2 não resultou em 4") 
    try: 
        assert square(3) == 9
    except AssertionError:
        print("A raiz de 3 não resultou em 9") 
    
if __name__ == "__main__":
    main()