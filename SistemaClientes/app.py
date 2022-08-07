import database
import datetime
MENU_PROMPT = """------ MENU ------

Elija una opción:

1. Agregar cliente
2. Mostrar clientes
3. Buscar cliente
4. Buscar cliente por DNI
5. Agregar venta
6. Mostrar ventas por cliente
7. Mostrar todas las ventas
8. Agregar cliente y venta
9. Agregar Producto
10. Mostrar Productos
11. Salir

Su eleccion:"""

def menu():
    connection =database.connect()
    database.createTables(connection)
    
    while (user_input := input(MENU_PROMPT)) != "11":
        if user_input == '1':
            prompt_add_client(connection)
        elif user_input == '2':
            prompt_get_clients(connection)            
        elif user_input == '3':
            prompt_search_client_by_name(connection)     
        elif user_input == '4':
            prompt_search_client_by_dni(connection)           
        elif user_input == '5':
            prompt_add_venta(connection)      
        elif user_input == '6':
            prompt_get_ventas_by_cliente(connection)   
        elif user_input == '7':
            prompt_get_ventas_data_clientes(connection) 
        elif user_input == '8':
            prompt_get_ventas_data_clientes(connection)   
        elif user_input == '9':
            prompt_add_product(connection)
        elif user_input == '10':
            prompt_get_products(connection)   
                                             
        else:
            print("Opción inválida")

#opcion 1
def prompt_add_client(connection):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("(Opcional) Telefono: ")
    direccion = input("(Opcional) Direccion: ")
    dni = int(input("DNI: "))
    database.addClient(connection, nombre, apellido, telefono, direccion,dni)    
#opcion 2    
def prompt_get_clients(connection):
    clients = database.getClients(connection)
    for client in clients:
        print(client)
#opcion 3                
def prompt_search_client_by_name(connection):
    nombre = input("Nombre: ")
    clients = database.getClientsByName(connection, nombre)
    if len(clients) == 0:
        print('No se encontró ningún cliente con ese nombre')
    else:    
        for client in clients:
            print(client)    
#opcion 4
def prompt_search_client_by_dni(connection):
    dni = input("DNI: ")
    clients = database.getClientsByDni(connection, dni)
    if len(clients) == 0:
        print('No se encontró ningún cliente con ese DNI')
    else:    
        for client in clients:
            print(client)        
      
#opcion 5            
def prompt_add_venta(connection):
    fecha = input("Fecha dd/mm/aaaa (INGRESE H SI QUIERE INGRESAR LA FECHA ACTUAL): ")
    if fecha.lower() == 'h':
        fecha=datetime.datetime.now().strftime("%d/%m/%Y")
    monto_venta = float(input("Monto de la venta: "))
    
    cliente_id = int(input("ID del cliente: "))
    product_id = int(input("ID del producto: "))
    if database.getClientById(connection, cliente_id) is None or database.getProductosById(connection, product_id) is None:
        print("Cliente o producto no encontrado")
    else:
        database.addVenta(fecha, monto_venta, cliente_id, product_id)
        print("Venta agregada")
    
#opcion 6
def prompt_get_ventas(connection):
    ventas = database.getVentas(connection)
    if len(ventas) == 0:    
        print('No se encontró ninguna venta')
    else:    
        for venta in ventas:
            print(venta)
#opcion 7       
def prompt_get_ventas_data_clientes(connection):
    ventas = database.getClientDataVenta(connection)
    if len(ventas) == 0:    
        print('No se encontró ninguna venta')
    else:    
        for venta in ventas:
            print(venta)
                
      
def prompt_get_ventas_by_cliente(connection):
    cliente_id = input("ID del cliente: ")
    ventas = database.getVentasByClient(connection, cliente_id)
    if len(ventas) == 0:    
        print('No se encontró ninguna venta realizada al cliente')
    else:    
        for venta in ventas:
            print(venta)      


def prompt_add_product(connection):
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    database.addProducto(connection, nombre, precio)
    
def prompt_get_products(connection):
    products = database.getProductos(connection)
    if len(products) == 0:    
        print('No se encontró ningun producto')
    else:    
        for product in products:
            print(product)    
        
            
menu()    