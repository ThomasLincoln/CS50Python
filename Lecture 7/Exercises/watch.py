import re
import sys


def main():
    result = parse(input("HTML: "))
    if result != None:
        print(f"https://youtu.be/{result}")
    else: 
        print(result)


def parse(s):
    pattern = r"https?://www\.youtube\.com/(?:embed)?/([\w]+)"
    matches = re.search(pattern, s)
    if matches:
        return matches.group(1)
    


if __name__ == "__main__":
    main()