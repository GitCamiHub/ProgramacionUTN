import functions
members = {
    'Socio n°1':['AMANDA NUÑEZ', '17/03/2009', 'Cuota al dia'],
    'Socio n°2':['BARBARA MOLINA', '17/03/2009', 'Cuota al dia'],
    'Socio n°3':['LAUTARO CAMPOS', '17/03/2009','Cuota al dia'],
}

while True:
    print('\nOpciones:\n1. Cargar socio\n2. Cantidad de socios registrados\n3. Registrar pago de cuotas adeudadas\n4. Modificar fecha de ingreso\n5. Dar de baja\n6. Ver listado de socios\n7. Salir')
    option = int(input("Elegir opcion: "))
    print(" ")
    if option in (1,2,3,4,5,6,7):
        if option == 1:
            member_data = list(functions.add_member())
            last_member_key = functions.last_member_key(members)
            members['Socio n°'+str(last_member_key+1)] = member_data

        elif option == 2:
            print("En este momento el club cuenta con", len(members), 'socios/as.')
            
        elif option == 3:
            member_key = functions.fee_payment(members)
            if member_key != '0':
                print("\nModificacion realizada con exito.")
                print(members.get(member_key))
            else:
                print("\nNo se encontró ese numero de socio/a.")
            
        elif option == 4:
            print("\nEl programa buscará si algun/a socio/a ingresó el 13/03/2018 y lo cambiará por el 14/03/2018.")
            date_search = functions.date_search(members)
            if date_search != 0:
                print(f"Se modificaron {date_search} fechas")
            else:
                print("Ningun usuario ingresó el 13/03/2018.")

        elif option == 5:
            member_search = functions.eliminate_member(members)
            if member_search != '0':
                print(f"La/El socia/o {member_search} fue eliminada/o.")
            else:
                print("El nombre no fue encontrado.")
                
        elif option == 6:
            for member, data in members.items():
                print(member,data)

        elif option == 7:
            print("\nSaliendo")
            break
    else:
        print("Ingrese una opcion correcta.")