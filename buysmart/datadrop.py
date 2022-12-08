import sqlite3
from multiprocessing import connection

connection = sqlite3.connect(
    "C:/Users/ASUS/Documents/GitHub/Buysmart/buysmart/data_buysmart.db")

connection.execute("DELETE FROM Carnes WHERE Precio is null")
