class Motocicleta:
    estado = 'Nueva'
    motor = False

    def __init__(self,color,matricula,combustible_litros,numero_ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = 10
        self.numero_ruedas = 2
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso

    def arrancar(self):
        if self.motor == False:
            self.motor = True
            print('Motor encendido.')
        else:
            print('El motor ya está encendido.')

    def detener(self):
        if self.motor == True:
            self.motor = False
            print('Se apagó el motor.')
        else:
            print('El motor ya estaba apagado.')

    def consultar_precio(self):
        print(f'El precio de la motocicleta {self.marca} {self.modelo} es de ${self.precio}.')
    