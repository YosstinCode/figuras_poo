class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC) :
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def base(self):
        return max([self.ladoA, self.ladoB, self.ladoC])

    def altura(self):
       return (2*self.area()) / self.base()

    def area(self):
        #formula de heron's
        s = self.perímetro() / 2
        return (s * (s - self.ladoA) * (s - self.ladoB) * (s - self.ladoC)) ** 0.5

    def perímetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    
    def tipo(self):
        if self.ladoA == self.ladoB == self.ladoC:
            return "Equilatero"
        elif self.ladoA == self.ladoB or self.ladoA == self.ladoC or self.ladoB == self.ladoC:
            return "Isosceles"
        else:
            return "Escaleno"
        

    
