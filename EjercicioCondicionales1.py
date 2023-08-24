# Pedimos que el usuario ingrese una fecha.
fecha = input('Ingrese la fecha en formato dia,DD/MM: ')

# Extraemos el dia de la semana, el numero de dia y el mes usando metodos para string.
dia_semana= fecha[0:fecha.find(',')].lower()
dia = int(fecha[fecha.find(',')+1:fecha.find('/')])
mes = int(fecha[fecha.find('/')+1:len(fecha)])

# Si el dia y/o el mes son numeros invalidos se muestra un mensaje.
if (dia>31 or dia<1 or mes>12 or mes<1):
    print('Ingrese una fecha correcta')   

# Colocamos las intrucciones que deben llevarse a cabo si el dia de la semana es lunes, martes o miercoles.
elif(dia_semana == 'lunes' or dia_semana == 'martes' or dia_semana =='miercoles'):
    # Preguntamos si el dia ingresado hubo examenes.
    si_examen = input('¿Este dia hubo examenes? (si/no): ').lower()
    # Colocamos las instrucciones que deben llevarse a cabo si la respuesta es si.
    if (si_examen == 'si'):
        # Le pedimos al usuario que ingrese la cantidad de alumnos aprobados y desaprobados.
        aprobados = int(input('Cantidad de alumnos aprobados: '))
        desaprobados = int(input('Cantidad de alumnos desaprobados: '))
        # Calculamos el total de alumnos para luego calcular y mostrar el porcentaje de aprobados.
        total_alumnos = aprobados + desaprobados
        porcentaje_apobados = (aprobados*100)/total_alumnos
        print('Porcentaje de aprobados:', porcentaje_apobados)

# Colocamos las intrucciones que deben llevarse a cabo si el dia de la semana es jueves: práctica hablada.
elif(dia_semana == 'jueves'):
    # Le pedimos al usuario que ingrese el porcentaje de asistencia a las clases.
    asistencia = float(input('Ingrese el porcentaje de asistencia: '))
    # Mostramos por pantalla un mensaje segun el valor del porcentaje de asistencia.
    if(asistencia>50):
        print('Asistio la mayoria.')
    else:
        print('No asistio la mayoria.')

# Colocamos las intrucciones que deben llevarse a cabo si el dia de la semana es viernes y tanto el dia como el mes
# cumplen las condiciones.
elif(dia_semana == 'viernes' and dia == 1 and (mes == 1 or mes==7)):
    print('Comienzo de nuevo ciclo.')
    # Le pedimos al usuario que ingrese la cantidad de alumnos en el ciclo nuevo y el arancel por cada uno
    # para luego calcular el ingreso total y mostrarlo por pantalla.
    cant_alumnos = int(input('Ingrese la cantidad de alumnos del ciclo nuevo: '))
    arancel = float(input('Ingrese el arancel por alumno: '))
    print('El ingreso total es de $', cant_alumnos*arancel)

# Si el dia de la semana no corresponde con ninguno de los evaluados anteriormente se imprime un mensaje.
else:
    print('Ingrese un dia de la semana correcto')
    
    
    