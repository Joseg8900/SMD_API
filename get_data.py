import requests
from json_format import format
from key import KEY

ENDPOINT: str = "https://data.alpaca.markets/v2/stocks/bars?symbols="
FORMAT: str = "&timeframe=1D&start=2020-01-01&end=2025-01-01&limit=1&adjustment=raw&feed=sip&sort=asc"

def get(tickr: str):

    STOCK = ENDPOINT+ tickr + FORMAT

    response: requests = requests.get(STOCK, headers = KEY)
    return response.json()