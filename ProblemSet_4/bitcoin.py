import requests
# import json
import sys

try:
    if len(sys.argv) !=2 :
        sys.exit("Missing command-line argument")
    try: 
        amount = float(sys.argv[1])
    
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        o = response.json()
        currency = o["bpi"]["USD"]["rate_float"]
        total_amount = amount * currency

    except ValueError:
        sys.exit("Command-line argument is not a number") 

except requests.RequestException:
    sys.exit("Command-line argument is not a number")

print(f"${total_amount:,.4f}")