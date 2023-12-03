# class Cat:
#     MEOWS = 3
    
#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")

# cat = Cat()
# cat.meow()

# Docstring
# def meow(n: int):
#     """
#     Meow n times.
    
#     :param n: Number of times do meow
#     :type n: int
#     """
#     return "meow\n" * n

# number: int = input("Number: ")
# meows: str = meow(number)
# print(meows, end="")
#----------------------------------------


# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py")

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="Number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
  print("meow")
