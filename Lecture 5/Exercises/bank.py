def main():
    greeting = input()
    response = value(greeting)
    print(response)


def value(greeting):
    search_for_Hello = greeting.find("Hello")
    search_for_H = greeting.find("H")

    if search_for_Hello == 0:
        return "$0"
    elif search_for_H == 0:
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
