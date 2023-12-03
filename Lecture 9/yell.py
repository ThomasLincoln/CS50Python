def main():
    """
        Main function
    """
    yell("This", "is", "CS50")

def yell(*palavras):
    """
        print words in uppercase
    """
    uppercased = map(str.upper, palavras)
    print(*uppercased)

if __name__ == "__main__":
    main()
