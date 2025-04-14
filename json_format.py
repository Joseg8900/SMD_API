import json

def format(stock_raw: dict):

    format = json.dumps(stock_raw.get("bars",{}))
    return format
