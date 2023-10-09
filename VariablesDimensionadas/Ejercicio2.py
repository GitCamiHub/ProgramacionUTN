import functions

purchasers_list = [
    ('Susana Gimenez',25,50500,'Punta del Este 222'),
    ('Moria Casan',5,31400,'Corrientes 5301'),
    ('Alejandro Sergi',15,80000,'Alvear 372'),
    ('Moria Casan',20,12800,'Corrientes 5301'),
    ('Ricardo Darin',10,45600,'Patricias 1349'),
]

while True:
    print("\n1.Ver datos de los clientes del mes.\n2.Obtener domicilios para envio de factura\n3.Salir")
    option = int(input("Elegir una opcion: "))
    print(" ")
    if option==1:
        for i in purchasers_list:
            print(i)
    elif option==2:
        client_address_set = functions.clients_address(purchasers_list)
        for i in client_address_set:
            print(i)
    elif option==3:
        print("Saliendo")
        break
    else:
        print("Ingrese una opcion correcta.")