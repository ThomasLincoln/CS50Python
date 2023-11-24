import re

email = input("Qual é o seu email?").strip()

if re.search(r"^(\w|\s)+@(\w|\s)+\.(edu|com|br|gov)$", email, re.IGNORECASE):
    print("Valid")
else: 
    print("Invalid")