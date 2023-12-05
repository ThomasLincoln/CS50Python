def main():
    time = input("What time is it? ")
    hour_converted = convert(time)
    if  hour_converted >= 7 and hour_converted <= 8:
        print("breakfast time")
    elif  hour_converted >= 12 and hour_converted <= 13:
        print("lunch time")
    elif  hour_converted >= 18 and hour_converted <= 19:
        print("dinner time")


def convert(time):
    parts = time.split(":", 2)
    return float(parts[0]) + float(parts[1])/60


if __name__ == "__main__":
    main()
