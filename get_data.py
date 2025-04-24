import requests
import json
import os
from key import KEY

ENDPOINT: str = "https://data.alpaca.markets/v2/stocks/bars?symbols="
FORMAT: str = "&timeframe=1D&start=2020-01-01&end=2025-01-01&limit=2000&adjustment=raw&feed=sip&sort=asc"

def get(tickr: str):
    #concatenates the full url that will be sent.
    STOCK = ENDPOINT+ tickr + FORMAT

    #Uses the request.get(url) to fetch data from the Alpaca server
    response = requests.get(STOCK, headers = KEY)
    data = json.response.json()

    file_path = os.path.join("json",f"{tickr}.json")

    with open(file_path,"w") as f:
        json.dump(data,f,indent=4)
    print(f"Data for {tickr} saved to file{file_path}.")