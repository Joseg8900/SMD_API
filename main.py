from get_data import get
import json

#with open('stocks.txt',"r") as file:


# Open and loads the JSON file.
stock: dict = {}
with open('data1.json', 'r') as file:
    stock = json.load(file)


#Takes ticker str and creates a csv file with the fields.
print("DateTime,Open,Close,High,Low")
for field in stock[Ticker]:
    print(f"{field['t'][0:10]},{field['o']},{field['c']},{field['h']},{field['l']}")