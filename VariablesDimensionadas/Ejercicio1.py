import functions

passengers_list = []
cities_list = []

while True:
    print("\nOpciones:")
    print("1. Agregar pasajero\n2. Agregar ciudad\n3. Consultar ciudad de destino de pasajero\n4. Cantidad de pasajeros que viajan a ciudad\n5. Consultar pais de destino\n6. Cantidad de pasajeros que viajan a pais\n7. Salir")
    option = input("Elija una opción: ")

    if option in ('1','2','3','4','5','6','7'):
        if option == '1':
            passengers_list.append(functions.add_people())
        elif option == '2':
            cities_list.append(functions.add_city())
        elif option == '3':
            city_destination= functions.destination_city(passengers_list)
            if city_destination!="0":
                print(f"El pasajero se dirije a {city_destination}")
            else:
                print(f"Dni no encontrado.")
        elif option == '4':
            input_city = input("Ingrese una ciudad para saber cuantos pasajeros viajan: ").upper()
            print(f"Cantidad de pasajeros: {functions.city_passengers_count(passengers_list,input_city)}")
        elif option == '5':
            functions.destination_country(passengers_list, cities_list)
        elif option == '6':
            print(f"Cantidad de pasajeros: {functions.country_passengers_count(passengers_list,cities_list)}")
        elif option == '7':
            print("Hasta la proxima.")
            break
    else:
        print("Ingrese una opcion correcta.")
    
