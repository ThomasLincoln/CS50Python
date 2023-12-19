import os
import argparse
import sys

def main():

    args = get_arg()
    text = get_text_from_user(args)
    os.system('clear')
    response = "0"
    while response != "-5":
        os.system('clear')
        print_options()
        response = input("Option:")
        match response:
            case "1":
                total_words = count_words(text)  # pylint: disable=invalid-name
                print(f"Total Words: {total_words}")
            case "2":
                total_letters = count_letters(text)    # pylint: disable=invalid-name
                print(f"Total Letters: {total_letters}")
            case "3":
                total_paragraphs = count_paragraphs(text)  # pylint: disable=invalid-name
                print(f"Total Paragraphs: {total_paragraphs}")
            case "4":
                total_lines = count_lines(text)
                print(f"Total Lines: {total_lines}")
            case "5":
                frequencies = word_frequencies(text)
                for word, frequency in frequencies.items():
                    print(f"{word}: {frequency}")
            case "6":
                word_input = input("Which word? ")
                frequency = word_frequency(text, word_input)
                for word, freq in frequency.items():
                    print(f"{word}: {freq}")
            case "7":
                show_text(text)
            case "-1":
                sys.exit("Goodbye")
            case _:
                input("Press Enter to continue...")
        input("Press Enter to continue...")


def print_options():
    print("1 - Number of Words")
    print("2 - Number of Letters")
    print("3 - Number of Paragraphs")
    print("4 - Number of Lines")
    print("5 - Word Frequencies")
    print("6 - Frequency of a Specific Word")
    print("7 - Show Text")
    
    print("-1 - Exit")

def show_text(text):
    print(text)


def word_frequency(text, input_word):
    text_without_punctuation = text.replace(',', ' ').replace('.', ' ')
    
    words = text_without_punctuation.split()
    frequency = {}
    frequency[input_word] = 0
    for word in words:
        if word == input_word:
            if word in frequency:
                frequency[word] += 1
    return frequency

def word_frequencies(text):
    text_without_punctuation = text.replace(',', ' ').replace('.', ' ')
    
    words = text_without_punctuation.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def get_text_from_user(args):
    if args.paste:
        with open(args.paste, 'r', encoding="UTF-8") as file:
            return file.read()
    else:
        return input("Text: ")


def get_arg():
    """
       Verify the user decision
    """
    parser = argparse.ArgumentParser(
        description="A program to analyse a Text")
    parser.add_argument("--paste", default=0, help="Use a .txt")
    return parser.parse_args()


def count_words(text):
    return len(text.split(" "))

def count_letters(text):
    texto = text.replace(',', '').replace('.', '')
    return len(texto)


def count_paragraphs(text):
    return len(text.split("\n"))

def count_lines(text):
    return len(text.split(".")) - 1


if __name__ == "__main__":
    main()
