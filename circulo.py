import math

class Circulo:
    def area(self):
        raio = float(input("Digite o raio do Circulo: "))
        return math.pi * (raio ** 2)