class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.base = None
        self.ladoC = ladoC
        self.ladoA = ladoA
        self.ladoB = ladoB

    def set_base(self, base):
        self.base = base

    def calcular_base(self):
        if self.base:
            return self.base
        else:
            return max(self.ladoA, self.ladoB, self.ladoC)

    def altura(self):
        if self.base:
            return (2*self.area()) / self.base
        else:
            return (2*self.area()) / self.calcular_base()

    def area(self):
        s = self.perimetro() / 2
        return (s*(s-self.ladoA)*(s-self.ladoB)*(s-self.ladoC))**0.5

    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def tipo(self):
        if self.ladoA == self.ladoB == self.ladoC:
            return "Equilatero"
        elif self.ladoA == self.ladoB or self.ladoA == self.ladoC or self.ladoB == self.ladoC:
            return "Isosceles"
        else:
            return "Escaleno"
