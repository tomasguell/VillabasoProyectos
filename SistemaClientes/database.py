import sqlite3 as sql
def connect():
    return sql.connect('database.db')



CREATE_CLIENT_TABLE = "CREATE TABLE if not exists Clientes (id integer primary key, nombre text, apellido text,telefono text DEFAULT NULL, direccion text DEFAULT NULL,dni integer);"

INSERT_CLIENT = "INSERT INTO Clientes (nombre, apellido, telefono, direccion, dni) VALUES (?,?,?,?,?);"

GET_CLIENTS = "SELECT * FROM Clientes;"

GET_CLIENTS_BY_NAME = "SELECT * FROM Clientes WHERE nombre = ?;"

GET_CLIENTS_BY_DNI = "SELECT * FROM Clientes WHERE dni = ?;"
def createTables(connection):  

    with connection:
        connection.execute(CREATE_CLIENT_TABLE)
        
def addClient(connection, nombre, apellido, telefono, direccion,dni):
    with connection:
        connection.execute(INSERT_CLIENT, (nombre, apellido, telefono, direccion,dni))    
        

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
                