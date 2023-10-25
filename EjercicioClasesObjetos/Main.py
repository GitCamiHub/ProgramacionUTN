from Motocicleta import Motocicleta

#Instancia de dos motocicletas
moto1 = Motocicleta('Negro','AEF512',10,2,'Zanella',2020,'12/03/2019',200,100)
moto2 = Motocicleta('Blanco','BCF212',15,3,'Honda',2022,'20/05/2022',180,110)

print(moto2.combustible_litros, moto2.numero_ruedas)

#Metodos arrancar y detener
moto1.arrancar()
moto1.arrancar()
moto1.detener()
moto2.detener()

#Creación dinámica de un atributo
moto1.precio = 2500
print(f'El precio de la motocicleta {moto1.marca} {moto1.modelo} es de ${moto1.precio}.')

#Consultar precio desde metodo
moto1.consultar_precio()
'''moto2.consultar_precio() Tira error porque no tiene ese valor definido'''

