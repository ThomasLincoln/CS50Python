from sys import argv
import sys
import requests

numero_de_bitcoins = 0

if len(argv) < 1:
    print("Missing command-line argument")
try:
    numero_de_bitcoins = float(argv[1])
except:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    bpi = response["bpi"]
    usd = bpi['USD']
    rate = usd["rate_float"]
    print(f"${rate * numero_de_bitcoins:,.4f}")
except requests.RequestException:
    pass
