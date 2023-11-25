import re

name = input("Qual é o seu nome?").strip()
matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    last, first = matches.group()
    name = (f"{first} {last}")
print(f"Hello, {name}")