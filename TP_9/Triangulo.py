class Triangulo:


    def __init__(self, lado1, lado2, lado3):


        #Atributos de instancia
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
       
    def imprimir_lado_mayor(self):
        max_lado = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado con tamaño mayor es: {max_lado}")


    def determinar_tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles")
        else:
            print("El triángulo es escaleno")