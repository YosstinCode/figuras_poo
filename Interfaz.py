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
            5. ver los valores ingresados.
            ################################
            0. para salir del menu circulo x'd
            """)

            opc = input('Ingrese la opcion que desea: ')

            try:
                opc = int(opc)
            except:
                opc = 6
            if opc > 5:
                print("Valor de opcion no valida")
            elif opc == 0:
                salir = True
            else:
                self.opciones_circulo(opc)

    def opciones_circulo(self, opc):
        match opc:
            case 1:
                angulo = self.recibir_flotante(
                    "Por favor ingrese el valor del angulo para calcular el arco si no desea realizar este calculo poner 0: ")
                radio = self.recibir_flotante(
                    "Por favor, ingrese el valor del radio: ")
                self.circulo = Circulo(angulo, radio)
            case 2:
                if self.circulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del area es el siguiente:")
                    print(f'{self.circulo.area()} m^2')

            case 3:
                if self.circulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del perimetro es el siguiente:")
                    print(f'{self.circulo.perimetro()} m')

            case 4:
                if self.circulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del arco es el siguiente:")
                    print(f'{self.circulo.arco()}')

            case 5:
                if self.circulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("Los valores ingresados son los siguientes:")
                    print(f'Angulo: {self.circulo.angulo}')
                    print(f'Radio: {self.circulo.radio}')

        os.system('pause')

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
            4. Hallar diagonal.
            5. ver los valores ingresados.
            ################################
            0. para salir del programa x'd
            """)

            opc = input('Ingrese la opcion que desea: ')

            try:
                opc = int(opc)
            except:
                opc = 6
            if opc > 5:
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

            case 3:
                if self.rectangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del perimetro es el siguiente:")
                    print(f'{self.rectangulo.perimetro()} m')

            case 4:
                if self.rectangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado de la diagonal es el siguiente:")
                    print(f'{self.rectangulo.diagonal()} m')

            case 5:
                if self.rectangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print('Los valores ingresados son los siguientes:')
                    print(f'Base: {self.rectangulo.base}')
                    print(f'Altura: {self.rectangulo.altura}')
        os.system('pause')

    def menu_triangulo(self):
        salir = False
        while not salir:

            os.system('cls')

            print("""
            Menu de triangulo.
            ################################
            1. Ingresar los valores.
            2. Ingresar base.
            3. Hallar el area.
            4. Hallar el perimetro.
            5. Hallar la base(en dado caso que no se ingrese).
            6. Hallar la altura.
            7. Hallar el tipo de triangulo.
            8. ver los valores ingresados.
            ################################
            0. para salir del programa x'd
            """)

            opc = input('Ingrese la opcion que desea: ')

            try:
                opc = int(opc)
            except:
                opc = 9
            if opc > 8:
                print("Valor de opcion no valida")
                os.system('pause')
            elif opc == 0:
                salir = True
            else:
                self.opciones_triangulo(opc)

    def menu_selecionar_base(self):
        os.system('cls')
        salir = False

        while not salir:

            os.system('cls')

            print(f"""
            Seleccione la base que desea calcular.
            ################################
            1. Lado A[{self.triangulo.ladoA} m].
            2. Lado B[{self.triangulo.ladoB} m].
            3. Lado C[{self.triangulo.ladoC} m].
            ################################
            0. para salir del menu de seleccion de base. x'd
            """)

            opc = input('Ingrese la opcion que desea: ')

            try:
                opc = int(opc)
            except:
                opc = 4
            if opc > 3:
                print("Valor de opcion no valida")

            elif opc == 0:
                salir = True
            else:
                salir = self.opciones_selecionar_base(opc)

    def opciones_selecionar_base(self, opc):
        match opc:
            case 1:
                print('La base ha sido seleccionada como el lado A')
                self.triangulo.set_base(self.triangulo.ladoA)
            case 2:
                print('La base ha sido seleccionada como el lado B')
                self.triangulo.set_base(self.triangulo.ladoB)
            case 3:
                print('La base ha sido seleccionada como el lado C')
                self.triangulo.set_base(self.triangulo.ladoC)

        return True

    def opciones_triangulo(self, opc):
        match opc:
            case 1:
                ladoA = self.recibir_flotante(
                    "Por favor ingrese el valor del lado A: ")
                ladoB = self.recibir_flotante(
                    "Por favor, ingrese el valor del lado B: ")
                ladoC = self.recibir_flotante(
                    "Por favor, ingrese el valor de la lado C: ")

                self.triangulo = Triangulo(ladoA, ladoB, ladoC)
            case 2:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    self.menu_selecionar_base()
            case 3:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del area es el siguiente:")
                    print(f'{self.triangulo.area()} m^2')

            case 4:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del perimetro es el siguiente:")
                    print(f'{self.triangulo.perimetro()} m')

            case 5:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado de la base es el siguiente:")
                    print(f'{self.triangulo.calcular_base()} m')

            case 6:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado de la altura es el siguiente:")
                    print(f'{self.triangulo.altura()} m')

            case 7:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del tipo de triangulo es el siguiente:")
                    print(f'{self.triangulo.tipo()}')

            case 8:
                if self.triangulo is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print('Los valores ingresados son los siguientes:')
                    print(f'Lado A: {self.triangulo.ladoA}')
                    print(f'Lado B: {self.triangulo.ladoB}')
                    print(f'Lado C: {self.triangulo.ladoC}')
                    if self.triangulo.base:
                        print(f'Base: {self.triangulo.base}')
                    else:
                        print(f'Base: {self.triangulo.calcular_base()}')

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
            4. Hallar diagonal.
            5. ver los valores ingresados.
            ################################
            0. para salir del programa x'd
            """)

            opc = input('Ingrese la opcion que desea: ')

            try:
                opc = int(opc)
            except:
                opc = 6
            if opc > 5:
                print("Valor de opcion no valida")
            elif opc == 0:
                salir = True
            else:
                self.opciones_cuadrado(opc)

    def opciones_cuadrado(self, opc):
        match opc:
            case 1:
                lado = self.recibir_flotante(
                    "Por favor ingrese el valor de unos de los lados del cuadrado: ")

                self.cuadrado = Cuadrado(lado)
            case 2:
                if self.cuadrado is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del area es el siguiente:")
                    print(f'{self.cuadrado.area()} m^2')

            case 3:
                if self.cuadrado is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del perimetro es el siguiente:")
                    print(f'{self.cuadrado.perimetro()} m')

            case 4:
                if self.cuadrado is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print("El resultado del arco es el siguiente:")
                    print(f'{self.cuadrado.diagonal()}')

            case 5:
                if self.cuadrado is None:
                    print("Por favor ingrese los valores primero")
                else:
                    print('Los valores ingresados son los siguientes:')
                    print(f'lados: {self.cuadrado.lado}')

        os.system('pause')

    def recibir_flotante(self, mensaje: str):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except:
                print("Debes ingresar un valor valido (decimal, entero).")
                os.system("pause")
