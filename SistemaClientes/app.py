import database

MENU_PROMPT = """------ MENU ------

Elija una opción:

1. Agregar cliente
2. Mostrar clientes
3. Buscar cliente
4. Buscar cliente por DNI
5. Salir

Su eleccion:"""

def menu():
    connection =database.connect()
    database.createTables(connection)
    
    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == '1':
            prompt_add_client(connection)
        elif user_input == '2':
            prompt_get_clients(connection)            
        elif user_input == '3':
            prompt_search_client_by_name(connection)     
        elif user_input == '4':
            prompt_search_client_by_dni(connection)           
        else:
            print("Opción inválida")


def prompt_add_client(connection):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Telefono: ")
    direccion = input("Direccion: ")
    dni = int(input("DNI: "))
    database.addClient(connection, nombre, apellido, telefono, direccion,dni)    
    
def prompt_get_clients(connection):
    clients = database.getClients(connection)
    for client in clients:
        print(client)
                
def prompt_search_client_by_name(connection):
    nombre = input("Nombre: ")
    clients = database.getClientsByName(connection, nombre)
    if len(clients) == 0:
        print('No se encontró ningún cliente con ese nombre')
    else:    
        for client in clients:
            print(client)    

def prompt_search_client_by_dni(connection):
    dni = input("DNI: ")
    clients = database.getClientsByDni(connection, dni)
    if len(clients) == 0:
        print('No se encontró ningún cliente con ese DNI')
    else:    
        for client in clients:
            print(client)        
menu()    