class Jar:
    def __init__(self, capacity=12):
        if(capacity < 0):
            raise ValueError("Capacity needs to be a positive integer")
        self._capacity = capacity
        self._quantity = 0
        

    def __str__(self):
        cookies = "🍪" * self._quantity
        return cookies

    def deposit(self, n):
        tentativa = self._quantity + n
        if(tentativa > capacity):
            raise ValueError(f"You can't add {n} cookies")
        self._quantity = tentativa
        

    def withdraw(self, n):
        if self._quantity < 0:
            raise ValueError("You don't have cookies")
        self._quantity = self._quantity - n
        if self._quantity < 0:
            self._quantity = 0

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._quantity
