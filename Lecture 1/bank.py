response = input()

search_for_Hello = response.find("Hello")
search_for_H = response.find("H")

if search_for_Hello == 0:
    print("$0")
elif search_for_H == 0:
    print("$20")
else:
    print("$100")
