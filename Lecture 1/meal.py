def main():
    time = input("What time is it? ")
    parts = time.rsplit(":", 2)
    hour_converted = convert(parts)
    if  hour_converted >= 7 and hour_converted <= 8:
        print("breakfast time")
    elif  hour_converted >= 12 and hour_converted <= 13:
        print("lunch time")
    elif  hour_converted >= 18 and hour_converted <= 19:
        print("dinner time")


def convert(time):
    return float(time[0]) + float(time[1])/60


if __name__ == "__main__":
    main()
