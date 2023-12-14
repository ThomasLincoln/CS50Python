import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    rangeAux = r"([0-9]|[1-9][0-9]|[0-1][0-9][0-9]|2[0-4][0-9]|25[0-5])"
    ip_pattern = fr"^{rangeAux}\.{rangeAux}\.{rangeAux}\.{rangeAux}$"

    matchs = re.search(ip_pattern, ip)

    if not matchs:
        return False
    if matchs.group(1):
        if int(matchs.group(1)) > 255:
            return False
    if matchs.group(2):
        if int(matchs.group(2)) > 255:
            return False
    if matchs.group(3):
        if int(matchs.group(3)) > 255:
            return False
    if matchs.group(3):
        if int(matchs.group(4)) > 255:
            return False
    return True
        


if __name__ == "__main__":
    main()