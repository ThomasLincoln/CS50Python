meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

flag = True
while flag == True:
    data = input("Date: ").strip()

    if "/" in data:
        date_parts = data.split("/")
        year = date_parts[2]
        month = date_parts[0].zfill(2)
        day = date_parts[1].zfill(2)
        if month.isnumeric():
            if 0<=int(month)<=12 and 1<=int(day)<=31:
                print(f"{year}-{month}-{day}")
                flag = False

    elif " " in data:
        date_parts = data.split(" ")
        year = date_parts[2]
        month_name = date_parts[0]
        day = date_parts[1][:-1].zfill(2)
        if day.isnumeric():
            if 1<=int(day)<=31 and data.find(",") != -1:
                # print(day, month_name, year)
                # print(meses.index(month_name) + 1) 
            
                try:
                    month = meses.index(month_name) + 1
                    month = str(month).zfill(2)
                    print(f"{year}-{month}-{day}")
                    flag = False
                except ValueError:
                    pass