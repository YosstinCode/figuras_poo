import os

from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Triangulo import Triangulo


class Interfaz:
    def __init__(self):
        self.circulo = None
        self.rectangulo = None
        self.triangulo = None
        self.cuadrado = None

    def menu(self):
        salir = False
        while not salir:
            os.system('cls')
            print("""
            Programa de cálculo geometrico.
            ################################
            1. Circulo.
            2. Rectangulo.
            3. Triangulo.
            4. Cuadrado.
            ################################
            0. para salir del programa x'd
            """)

            opc = input("Ingrese la opcion que desea: ")

            try:
                opc = int(opc)
            except:
                opc = 5

            if opc > 4:
                print("Valor de opcion no valida")
            elif opc == 0:
                os.system('cls')
                print("Chaituuu! :D")
                print("Gracias por usar el programa")
                salir = True
            else:
                self.opciones_figuras(opc)

    def opciones_figuras(self, opc):
        match opc:
            case 1:
                self.menu_circulo()
            case 2:
                self.menu_rectangulo()
            case 3:
                self.menu_triangulo()
            case 4:
                self.menu_cuadrado()

    def menu_circulo(self):
        salir = False
        while not salir:
            os.system('cls')
            print("""
            Menu del circulo.
            ################################
            1. Ingresar los valores.
            2. Hallar el area.
            3. Hallar el perimetro.
            4. Hallar el arco.
            ################################
            0. para salir del programa x'd
            """)

            opc = input('Ingrese la opcion que desea: ')

            try:
                opc = int(opc)
            except:
                opc = 5
            if opc > 4:
                print("Valor de opcion no valida")
            elif opc == 0:
                salir = True
            else:
                self.opciones_circulo(opc)

    def opciones_circulo(self, opc):
        match opc:
            case 1:
                angulo = self.recibir_flotante(
                    "Por favor ingrese el valor del angulo: ")
                radio = self.recibir_flotante(
                    "Por favor, ingrese el valor del radio: ")
                self.circulo = Circulo(angulo, radio)
            case 2:
                if self.circulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del area es el siguiente:")
                    print(f'{self.circulo.area()} m^2')
                os.system('pause')
            case 3:
                if self.circulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del perimetro es el siguiente:")
                    print(f'{self.circulo.perimetro()} m')
                os.system('pause')
            case 4:
                if self.circulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del arco es el siguiente:")
                    print(f'{self.circulo.arco()}')
                os.system('pause')

        pass

    def menu_rectangulo(self):
        salir = False
        while not salir:
            os.system('cls')
            print("""
            Menu del rectangulo.
            ################################
            1. Ingresar los valores.
            2. Hallar el area.
            3. Hallar el perimetro.
            ################################
            0. para salir del programa x'd
            """)

            opc = input('Ingrese la opcion que desea: ')

            try:
                opc = int(opc)
            except:
                opc = 5
            if opc > 4:
                print("Valor de opcion no valida")
            elif opc == 0:
                salir = True
            else:
                self.opciones_rectangulo(opc)

    def opciones_rectangulo(self, opc):
        match opc:
            case 1:
                base = self.recibir_flotante(
                    "Por favor ingrese el valor de la base: ")
                altura = self.recibir_flotante(
                    "Por favor, ingrese el valor de la altura: ")
                self.rectangulo = Rectangulo(base, altura)
            case 2:
                if self.rectangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del area es el siguiente:")
                    print(f'{self.rectangulo.area()} m^2')
                os.system('pause')
            case 3:
                if self.rectangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del perimetro es el siguiente:")
                    print(f'{self.rectangulo.perimetro()} m')
                os.system('pause')

    def menu_triangulo(self):
        salir = False
        while not salir:

            print("""
            Menu de triangulo.
            ################################
            1. Ingresar los valores.
            2. Hallar el area.
            3. Hallar el perimetro.
            4. Hallar la base.
            5. Hallar la altura.
            6. Hallar el tipo de triangulo.
            ################################
            0. para salir del programa x'd
            """)

            opc = input('Ingrese la opcion que desea: ')

            try:
                opc = int(opc)
            except:
                opc = 5
            if opc > 6:
                print("Valor de opcion no valida")
            elif opc == 0:
                salir = True
            else:
                self.opciones_triangulo(opc)

    def opciones_triangulo(self, opc):
        match opc:
            case 1:
                ladoA = self.recibir_flotante(
                    "Por favor ingrese el valor del lado A: ")
                ladoB = self.recibir_flotante(
                    "Por favor, ingrese el valor del lado B: ")
                ladoC = self.recibir_flotante(
                    "Por favor, ingrese el valor del lado C: ")

                self.triangulo = Triangulo(ladoA, ladoB, ladoC)
            case 2:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del area es el siguiente:")
                    print(f'{self.triangulo.area()} m^2')
                os.system('pause')
            case 3:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del perimetro es el siguiente:")
                    print(f'{self.triangulo.perimetro()} m')
                os.system('pause')
            case 4:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado de la base es el siguiente:")
                    print(f'{self.triangulo.base()} m')
                os.system('pause')
            case 5:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado de la altura es el siguiente:")
                    print(f'{self.triangulo.altura()} m')
                os.system('pause')
            case 6:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del tipo de triangulo es el siguiente:")
                    print(f'{self.triangulo.tipo()}')
                os.system('pause')

    def menu_cuadrado(self):
        salir = False
        while not salir:
            os.system('cls')
            print("""
            Menu del cuadrado.
            ################################
            1. Ingresar los valores.
            2. Hallar el area.
            3. Hallar el perimetro.
            4. Hallar el arco.
            ################################
            0. para salir del programa x'd
            """)

            opc = input('Ingrese la opcion que desea: ')

            try:
                opc = int(opc)
            except:
                opc = 5
            if opc > 4:
                print("Valor de opcion no valida")
            elif opc == 0:
                salir = True
            else:
                self.opciones_cuadrado(opc)

    def opciones_cuadrado(self, opc):
        match opc:
            case 1:
                base = self.recibir_flotante(
                    "Por favor ingrese el valor de la base: ")
                altura = self.recibir_flotante(
                    "Por favor, ingrese el valor de la altura: ")
                self.cuadrado = Cuadrado(base, altura)
            case 2:
                if self.cuadrado is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del area es el siguiente:")
                    print(f'{self.cuadrado.area()} m^2')
                os.system('pause')
            case 3:
                if self.cuadrado is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del perimetro es el siguiente:")
                    print(f'{self.cuadrado.perimetro()} m')
                os.system('pause')
            case 4:
                if self.cuadrado is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del arco es el siguiente:")
                    print(f'{self.cuadrado.arco()}')
                os.system('pause')

    def recibir_flotante(self, mensaje: str):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except:
                print("Debes ingresar un valor valido (decimal, entero).")
                os.system("pause")
