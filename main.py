from get_data import get
from database import *

tickr:str = 'MSFT'
stocks: dict = (get(tickr))
#print( stocks["bars"]["MSFT"])



# Now, 'stock' is a dictionary
#print("DateTime,Open,High,Low,Close,Volume,Count,WeightedAverage")
#for entry in stock["bars"]["MSFT"]:
#    print(f"{entry['t'][0:10]},{entry['o']},{entry['h']},{entry['l']},{entry['c']},{entry['v']},{entry['n']},{entry['vw']}")