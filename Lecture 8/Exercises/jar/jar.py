class Jar:
    def __init__(self, capacity=12):
        if(capacity > 0):
            self._capacity = capacity
            self._quantity = 0
        else:
            raise ValueError("Capacity needs to be a positive integer")
        

    def __str__(self):
        cookies = "🍪" * self._quantity
        return cookies

    def deposit(self, n):
        if n+self._quantity <= self.capacity:
            self._quantity += n
        else:
            raise ValueError(f"You can't add {n} cookies")
        

    def withdraw(self, n):
        if n <= self._quantity:
            self._quantity -= n
        else:        
            raise ValueError("You don't have cookies")        

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._quantity

