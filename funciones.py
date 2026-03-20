clients = ()
products = ()


def register_clients():
    global clients

    Id_client = input("Ingrese su identificacion: ")
    while not Id_client.isdigit():
        print("Error solo se permiten numeros")
        Id_client = input("Ingrese su identificacion: ")

    Name = input("Ingrese nombre del cliente: ")

    while not Name.isalpha():
        print("Error ingrese solo letras")
        Name = input("Ingrese nombre del cliente: ")

    Email = input("Ingrese su correo: ")

    while "@" not in Email or "." not in Email:
        print("Error ingrese un correo valido")
        Email = input("Ingrese su correo: ")

    client = {
        "Id_client": Id_client,
        "Name": Name,
        "Email": Email
    }

    clients = clients + (client,)

    return client


def register_products():
    global products

    Product_id = input("Ingrese el ID del producto: ")

    while not Product_id.isdigit():
        print("Error solo se permiten numeros")
        Product_id = input("Ingrese el ID del producto: ")

    Product_name = input("Ingrese el nombre del producto: ")

    while not Product_name.replace("", "").isalpha():
        print("Error ingrese solo letras")
        Product_name = input("Ingrese el nombre del producto: ")

    valid = False

    while valid == False:
        try:
            Unit_price = float(input("Ingrese el valor del precio unitario: "))

            if Unit_price > 0:
                valid = True

            else:
                print("El precio debe ser mayor a cero")

        except:
            print("Error ingrese numeros sin puntos ni comas")

    product = (Product_id, Product_name, Unit_price)

    products = products + (product,)

    valid = False

    while valid == False:
        try:
            quantity_product = int(input("Ingrese el valor del precio unitario: "))

            if quantity_product > 0:
                valid = True

            else:
                print("La cantidad debe ser mayor a cero")

        except:
            print("Error ingrese numeros sin puntos ni comas")


def total_delivery (price_unit, quantity ):
    return round(price_unit * quantity, 1) 

def creation_delivery():
    client = register_clients ()
    products = register_products ()
    total = total_delivery()

    delivery= {
        "client": client,
        "products": products,
        "total": total
    }
    
    print("pedido creado correctamente")
    print(delivery)
    

def consult_of_delivery ():
    print("consulta de productos: \n")

    if not delivery:
        print("no hay pedidos registrados \n")
        input("presione cualquier tecla para volver al menu: \n")
        return
    
    for i, d in enumerate(delivery, 1):
        print(f"{i}. {d('clients')} | {d('products')} | {d('total')}")
    input("presione cualquier tecla para volver al menu")
