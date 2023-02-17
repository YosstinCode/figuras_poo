class Cuadrado:
    
    def __init__(self, lados):
        self.lados = lados
    
    def calcular_area(self):
        return self.lados[0] * self.lados[1]

    def calcular_perímetro(self):
        return 2 * (self.lados[0] + self.lados[1])

    def calcular_diagonal(self):
        return (self.lados[0] ** 2 + self.lados[1] ** 2) ** 0.5