import sys
import requests
import json
if len(sys.argv)<2:
    sys.exit("Missing command-line argument")
elif not sys.argv[1].isdigit():
    sys.exit("Command-line argument is not a number")
else :
    try:
        url="https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        data = json.loads(response.text)
        usd_rate = data["bpi"]["USD"]["rate"]
    except requests.RequestException:
        sys.exit()

    n=float(sys.argv[1])
    print(f"${n * usd_rate:,.4f}")