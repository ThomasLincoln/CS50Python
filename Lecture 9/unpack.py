#
# ? Unpacking
# def total(galleons, sickles, knuts):
#     """
#     Calculate a total of knuts in a account
#     """
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100,50,25]
# coinsDic = {"galleons": 100, "sickles": 50, "knuts": 25}

# TOTALARR = total(*coins)
# TOTALDIC = total(**coinsDic)
# print(f"{TOTALDIC} Knuts")

# ? args e kwargs

def f(*args, **kwargs):
    """
        Aqui eu vou testar os args e kwargs como estudo
    """
    print("Positional:", args)
    print("Names:", kwargs)
f(galleons=100,sickles=50,knuts=5)
