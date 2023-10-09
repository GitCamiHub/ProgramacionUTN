
from datetime import datetime

#-----------------------------EJERCICIO 1------------------------------
# Opcion 1
def add_people():
    name = input("\nNombre y apellido: ").upper()
    dni = int(input("DNI sin puntos: "))
    destination = input("Destino: ").upper()

    passenger = name,dni,destination
    print(passenger)
    return passenger

# Opcion 2
def add_city():
    city = input("\nCiudad: ").upper()
    country = input("Pais: ").upper()

    city_country = city, country
    print(city_country)
    return(city_country)

# Opcion 3
def destination_city(passengers_list):
    requested_dni= int(input("\nDNI del pasajero: "))
    counter = 0
    for name, dni, city in passengers_list:
        if dni == requested_dni:
            counter+=1
            return city
    if counter==0:
        return "0"

# Opcion 4
def city_passengers_count(passengers_list, requested_city):
    counter=0
    for name, dni, city in passengers_list:
        if city == requested_city:
            counter+=1
    return counter
            
# Opcion 5
def destination_country(passengers_list, cities_list):
    requested_city = destination_city(passengers_list)
    if requested_city == "0":
        print("\nDni no encontrado.")
    else:
        counter=0
        for city, country in cities_list:
            if city == requested_city:
                counter +=1
                print(f"\nEl pasajero se dirige a {country}.")
                break
        if counter == 0:
                print("\nLa ciudad todavia no ha sido registrada.")

# Opcion 6
def country_passengers_count(passengers_list, cities_list):
    requested_country = input("\nIngrese pais para saber cuantos pasajeros viajan: ").upper()
    passengers_amount=0
    for city,country in cities_list:
        if country == requested_country:
            passengers_amount += city_passengers_count(passengers_list, city)
    return passengers_amount
    

#-----------------------------EJERCICIO 2-----------------------------------

def clients_address(_list):
    address_set=set()
    for name,day,amount,address in _list:
        address_set.add(address)

    return address_set

#-----------------------------EJERCICIO 3-----------------------------------

# Opcion 1
def add_member():
    
    while True:
        name = input("Nombre y apellido: ").upper()
        if name.isalpha():
            break
        else:
            print("Ingrese solo letras.")

    while True:
        date_input = input("Fecha actual? (s/n): ").lower()

        current_date = datetime.now()
        if date_input == 's':
            admission_date = datetime.strftime(current_date, '%d/%m/%Y')
            break
        elif date_input == 'n':
            while True:
                day = int(input('Dia: '))
                if day<1 or day>31:
                    print("Ingrese un dia valido")
                else:
                    day = day
                    break
            while True:
                month = int(input('Mes: '))
                if month<1 or month>12:
                    print("Ingrese un mes valido")
                else:
                    month = month
                    break
            while True:
                year = int(input('Año: '))
                if year<2009 or year>2023:
                    print("Ingrese un año valido")
                else:
                    year = year
                    break
            admission_date = datetime(year,month,day)
            admission_date = datetime.strftime(admission_date,'%d/%m/%Y')
            break
        else:
            print("Ingrese una opcion correcta.")

    while True:
        fee_input = input("Tiene la cuota al dia? (s/n): ").lower()
    
        if fee_input == 's':
            fee = "Cuota al dia"
            break
        elif fee_input == 'n':
            fee = "Debe cuota"
            break
        else:
            print("Ingrese una opcion correcta.")

    return (name,admission_date,fee)

def last_member_key(members_dic):
    for i in members_dic.keys():
        last_member = i
    last_number = int(last_member[len(last_member)-1])

    return last_number

# Opcion 3
def fee_payment(members_dic):
    member_number = input("Ingrese el numero de socio: ")
    for i in members_dic.keys():
        if i[len(i)-1] == member_number:
            member_data = list(members_dic.get(i))
            member_data[2] = 'Cuota al dia'
            members_dic[i] = member_data
            return i
        else:
            continue
    return '0'

# Opcion 4
def date_search(members_dic):
    counter = 0
    for i in members_dic.values():
        if i[1] == '13/03/2018':
            counter += 1
            print(i)
            i[1] = '14/03/2018'
            finding_key = get_keys_with_value(members_dic,i)
            members_dic[finding_key] = i
        else:
            continue
    return counter

def get_keys_with_value(dic, value):
    for key, val in dic.items():
        if val == value:
            return key
    return None
    
# Opcion 5
def eliminate_member(members_dic):
    name = input("Ingrese nombre y apellido del socio: ").upper()
    for i in members_dic.values():
        if i[0] == name:
            finding_key = ''.join(get_keys_with_value(members_dic,i))
            members_dic.pop(finding_key)
            return name
        else:
            continue
    return '0'

            
