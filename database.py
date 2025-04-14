import sqlite3

def main():
    #Opens connection to db and inits cursor
    conn = sqlite3.connect('stock_data.db')  
    cursor = conn.cursor()

    # Enable foreign key support (needed in SQLite)
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    return cursor


def cr_StockTable(cursor):
    """
    This function defines a SQL query to create a table named 'Stocks' with two columns:
    - ID (INTEGER, PRIMARY KEY): A unique integer for each stock.
    - Ticker (TEXT, NOT NULL): The stock ticker symbol (e.g., 'AAPL' for Apple).

    After executing the query to create the table, the function commits the changes to the
    database and closes the cursor connection. If the table is created successfully,
    a confirmation message will be printed.

    Args:
        cursor (sqlite3.Cursor)
    """


    create_StockTable: str = '''
    CREATE TABLE IF NOT EXISTS Stocks(
        ID INTEGER PRIMARY KEY,
        Ticker TEXT NOT NULL
    )
    '''
    cursor.execute(create_StockTable)

    # Commit changes and close connection
    cursor.commit()
    cursor.close()

    print("Successful!")


def in_StockTable(cursor,tckr):

    insert_StockTable: str ='''
        INSERT INTO Stocks (Ticker)
        VALUES (?)
    '''
    cursor.execute(insert_StockTable,(tckr,))

    # Commit changes and close connection
    cursor.commit()
    cursor.close()

    print("Successful!")


def cr_TckrTable(cursor,tckr):

    create_TckrTable: str = f'''
    CREATE TABLE IF NOT EXISTS {tckr}_data (
        DateTime TEXT NOT NULL PRIMARY KEY,
        Ticker TEXT NOT NULL,
        Open REAL,
        High REAL,
        Low REAL,
        Close REAL,
        Volume INTEGER,
        Count INTEGER,
        WeightedAverage REAL,
        FOREIGN KEY (Ticker) REFERENCES Stocks (Ticker)
    );
    '''
    cursor.execute(create_TckrTable)

    # Commit changes and close connection
    cursor.commit()
    cursor.close()

    print("Successful!")


def in_TckrTable(cursor,tckr,data):
    insert_TckrTable: str = f'''
        INSERT INTO {tckr}_data (DateTime, Ticker, Open, High, Low, Close, Volume, Count, WeightedAverage)
        VALUES ({data['t'][0:10]},{tckr},{data['o']},{data['h']},{data['l']},{data['c']},{data['v']},{data['n']},{data['vw']}")
    '''

    # Commit changes and close connection
    cursor.commit()
    cursor.close()

    print("Successful!")

