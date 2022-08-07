import sqlite3 as sql
def connect():
    return sql.connect('database.db')
    


CREATE_CLIENT_TABLE = "CREATE TABLE if not exists Clientes (id integer primary key, nombre text, apellido text,telefono text DEFAULT NULL, direccion text DEFAULT NULL,dni integer);"
CREATE_VENTAS_TABLE = "CREATE TABLE if not exists Ventas (id integer primary key,fecha date, monto_venta float, cliente_id integer,foreign key (cliente_id) references Clientes(id));"

INSERT_CLIENT = "INSERT INTO Clientes (nombre, apellido, telefono, direccion, dni) VALUES (?,?,?,?,?);"
INSERT_VENTA = "INSERT INTO Ventas (fecha, monto_venta, cliente_id) VALUES (?,?,?);"

GET_CLIENTS = "SELECT * FROM Clientes;"
GET_VENTAS = "SELECT * FROM Ventas;"

GET_CLIENTS_BY_NAME = "SELECT * FROM Clientes WHERE nombre = ?;"
GET_CLIENTS_BY_DNI = "SELECT * FROM Clientes WHERE dni = ?;"
GET_CLIENT_DATA_VENTA = "SELECT Ventas.cliente_id, Clientes.nombre, Clientes.apellido, Clientes.dni,Ventas.fecha, Ventas.monto_venta FROM Clientes INNER JOIN Ventas ON Clientes.id = Ventas.cliente_id;"
GET_VENTAS_BY_CLIENT = "SELECT Clientes.nombre, Clientes.apellido, Clientes.dni,Ventas.fecha, Ventas.monto_venta FROM Clientes INNER JOIN Ventas ON Clientes.id = Ventas.cliente_id WHERE Clientes.id = ?;"

def createTables(connection):  

    with connection:
        connection.execute("PRAGMA foreign_keys = ON;")
        connection.execute(CREATE_CLIENT_TABLE)
        connection.execute(CREATE_VENTAS_TABLE)
        
        
def addClient(connection, nombre, apellido, telefono, direccion,dni):
    with connection:
        connection.execute(INSERT_CLIENT, (nombre, apellido, telefono, direccion,dni))    

        
def addVenta(connection, fecha, monto_venta, cliente_id):
    with connection:
        connection.execute(INSERT_VENTA, (fecha, monto_venta, cliente_id))

def getVentas(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_VENTAS)
        return cursor.fetchall()

def getClients(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_CLIENTS)
        return cursor.fetchall()
    
def getClientsByName(connection, nombre):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_CLIENTS_BY_NAME, (nombre,))
        return cursor.fetchall()
    
def getClientsByDni(connection, dni):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_CLIENTS_BY_DNI, (dni,))
        return cursor.fetchall()    
                
def getClientDataVenta(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_CLIENT_DATA_VENTA)
        return cursor.fetchall()                
    
    
def getVentasByClient(connection, Id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_VENTAS_BY_CLIENT, (Id,))
        return cursor.fetchall()    