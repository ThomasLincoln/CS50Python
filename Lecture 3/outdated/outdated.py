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
    data = input("Date: ")
    if (data.find("/") != -1):
        date_parts = data.split("/")
        if(int(date_parts[1]) < 10) and (int(date_parts[0]) < 10):
            print(f"{date_parts[2]}-0{date_parts[0]}-0{date_parts[1]}")
        elif(int(date_parts[0]) < 10):
            print(f"{date_parts[2]}-0{date_parts[0]}-{date_parts[1]}")
        elif(int(date_parts[1]) < 10):
            print(f"{date_parts[2]}-{date_parts[0]}-0{date_parts[1]}")
        flag = False  
    elif (data.find(" ")):
        date_parts = data.split(" ")
        date_parts[1] = int(date_parts[1][:-1])
        for i in range(len(meses)):
            if meses[i] == date_parts[0]:
                if(i < 10) and (int(date_parts[1]) < 10):
                    print(f"{date_parts[2]}-0{i+1}-0{date_parts[1]}")
                    break
                elif(i < 10):
                    print(f"{date_parts[2]}-0{i+1}-{date_parts[1]}")
                    break
                elif(int(date_parts[1]) < 10):
                    print(f"{date_parts[2]}-{i+1}-0{date_parts[1]}")
                    break
        flag = False