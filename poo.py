import math

class FiguraGeometrica:
    def area(self):
        pass

class Triangulo(FiguraGeometrica):
    def area(self):
        base = float(input("Digite a base do Triangulo: "))
        altura = float(input("Digite a altura do Triangulo: "))
        return (base * altura) / 2

class Retangulo(FiguraGeometrica):
    def area(self):
        base = float(input("Digite a base do Retangulo: "))
        altura = float(input("Digite a altura do Retangulo: "))
        return base * altura
    
class Circulo(FiguraGeometrica):
    def area(self):
        raio = float(input("Digite o raio do Circulo: "))
        return math.pi * (raio ** 2)
    
class Quadrado(FiguraGeometrica):
    def area(self):
        lado = float(input("Digite o lado do quadrado: "))
        return lado ** 2
    
#criei tres instancias
triangulo = Triangulo() 
retangulo = Retangulo()
circulo = Circulo()
quadrado = Quadrado()

print('Área do triangulo: ', triangulo.area())
print("Área do retangulo: ", retangulo.area())
print("Área do circulo: ", circulo.area())
print("Área do quadrado: ",quadrado.area())
