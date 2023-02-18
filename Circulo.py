import math


class Circulo:

    def __init__(self, angulo, radio):
        self.angulo = angulo
        self.radio = radio

    def area(self):
        return (math.pi * self.radio**2)

    def perimetro(self):
        return (2 * math.pi * self.radio)

    def arco(self):
        if self.angulo > 360 and self.angulo < 0:
            return 0
        else:
            return ((2 * math.pi * self.radio * self.angulo)/360)
