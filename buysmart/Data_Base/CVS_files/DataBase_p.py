import sqlite3
from multiprocessing import connection
from os.path import split


CREATE_VEGETABLES_TABLE = """
CREATE TABLE IF NOT EXISTS Vegetales (
id INTEGER PRIMARY KEY, 
Producto TEXT, 
Precio TEXT, 
Supermercado_id INTEGER,
Imagen_url TEXT,
Url TEXT, 
FOREIGN KEY (Supermercado_id) REFERENCES Supermercados (Supermercado_id));"""


CREATE_MEATS_TABLE = """
CREATE TABLE IF NOT EXISTS Carnes (
id INTEGER PRIMARY KEY, 
Producto TEXT, 
Precio TEXT, 
Supermercado_id INTEGER,
Imagen_url TEXT,
Url TEXT,
FOREIGN KEY (Supermercado_id) REFERENCES Supermercados (Supermercado_id));"""


CREATE_DISPENSE_TABLE = """
CREATE TABLE IF NOT EXISTS Despensa (
id INTEGER PRIMARY KEY, 
Producto TEXT, 
Precio TEXT, 
Supermercado_id INTEGER,
Imagen_url TEXT,
Url TEXT,
FOREIGN KEY (Supermercado_id) REFERENCES Supermercados (Supermercado_id));"""

CREATE_SUPERMARKET_TABLE = """CREATE TABLE IF NOT EXISTS Supermercados (Supermercado_id INTEGER PRIMARY KEY, Nombre TEXT);"""

INSERT_Vegetales = "INSERT INTO Vegetales (producto, precio, Supermercado_id, Imagen_url, Url) VALUES (?, ?, ?, ?, ?);"
INSERT_Carnes = "INSERT INTO Carnes (producto, precio, Supermercado_id, Imagen_url, Url) VALUES (?, ?, ?, ?, ?);"
INSERT_Despensa = '''INSERT INTO Despensa (producto, precio, Supermercado_id, Imagen_url, Url) VALUES (?, ?, ?, ?, ?);'''

INSERT_SUPERMARKET = "INSERT INTO Supermercados (Nombre) VALUES (?);"

GET_ALL_VEGETABLES = "SELECT * FROM Vegetales;"
GET_ALL_MEATS = "SELECT * FROM Carnes;"
GET_ALL_DISPENSE = "SELECT * FROM Despensa;"

GET_VEGETABLES_BY_NAME = "SELECT * FROM Vegetales WHERE Producto = ?;"
GET_MEATS_BY_NAME = "SELECT * FROM Carnes WHERE Producto = ?;"
GET_DISPENSE_BY_NAME = "SELECT * FROM Despensa WHERE Producto = ?;"

# GET_BEST_PRODUCT_FOR_MEATS = """
# SELECT * FROM Carnes
# WHERE Producto = ?
# ORDER BY rating DESC
# LIMIT 1;"""

connection = sqlite3.connect("data_buysmart.db")


def create_tables(connection, table):
    with connection:
        connection.execute(table)


def add_item_carnes(connection, Producto, Precio, Supermercado, Imagen_url, Url):
    """
    Categorias: Vegetales, Carnes, Despensa
    """
    with connection:
        connection.execute(INSERT_Carnes,
                           (Producto, Precio, Supermercado, Imagen_url, Url))


def add_item_Vegetales(connection, Producto, Precio, Supermercado, Imagen_url, Url):
    """
    Categorias: Vegetales, Carnes, Despensa
    """
    with connection:
        connection.execute(INSERT_Vegetales,
                           (Producto, Precio, Supermercado, Imagen_url, Url))


def add_item_Despensa(connection, Producto, Precio, Supermercado, Imagen_url, Url):
    """
    Categorias: Vegetales, Carnes, Despensa
    """
    with connection:
        connection.execute(INSERT_Despensa,
                           (Producto, Precio, Supermercado, Imagen_url, Url))


def get_all_items(connection, table):
    with connection:
        return connection.execute(table).fetchall()


def get_items_by_name(connection, Categoria, name):
    with connection:
        return connection.execute(f"GET_{Categoria}_BY_NAME", (name,)).fetchall()


# def get_best_price_for_item(connection, name):
#     with connection:
#         return connection.execute(GET_BEST_PREPARATION_FOR_item, (name,)).fetchone()


create_tables(connection, CREATE_VEGETABLES_TABLE)
create_tables(connection, CREATE_MEATS_TABLE)
create_tables(connection, CREATE_DISPENSE_TABLE)
create_tables(connection, CREATE_SUPERMARKET_TABLE)

connection.execute('''INSERT INTO Supermercados (Nombre) VALUES ('D1');''')
connection.execute(
    '''INSERT INTO Supermercados (Nombre) VALUES ('La vaquita');''')

url = "C:/Users/ASUS/Documents/GitHub/Data_Base/CVS_files/"


def Open_file(file_name, calling_name):
    with open(url+file_name, errors="ignore") as calling_name:

        for i in calling_name:
            values = i.split(",")
            Producto = values[0]
            Precio = values[1].replace('$', '')
            Supermercado = values[2]
            Categoria = values[3]
            Imagen = values[4]
            Pagina = values[5]

            if Supermercado == "D1":
                Supermercado = 1
            elif Supermercado == "La vaquita":
                Supermercado = 2
            else:
                pass

            if Categoria == "Carnes":
                add_item_carnes(connection, Producto,
                                Precio, Supermercado, Imagen, Pagina)

            elif Categoria == "Vegetales y frutas":
                add_item_Vegetales(connection, Producto,
                                   Precio, Supermercado, Imagen, Pagina)

            else:
                add_item_Despensa(connection, Producto,
                                  Precio, Supermercado, Imagen, Pagina)


Open_file("PriceList_D1_Carnes.csv", "D1_Carnes")
Open_file("PriceList_Lavaquita_carnes.csv", "Lavaquita_carnes")

Open_file("PriceList_D1_Despensa.csv", "D1_Despensa")
Open_file("PriceList_Lavaquita_Despensa.csv", "Lavaquita_Despensa")


Open_file("PriceList_D1_Vegetales_and_Verduras.csv",
          "D1_Vegetales_and_Verduras")
Open_file("PriceList_Lavaquita_vegetales.csv", "Lavaquita_vegetales")



####################################################################################################################################

#Queda faltando hacer limpieza de los datos en cada una de las tablas ya que en estas algunos productos tienen información faltante

#####################################################################################################################################