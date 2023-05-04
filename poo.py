import math
from triangulo import Triangulo

from quadrado import Quadrado

from retangulo import Retangulo

from circulo import Circulo


triangulo = Triangulo() 
retangulo = Retangulo()
circulo = Circulo()
quadrado = Quadrado()

print('Área do triangulo: ', triangulo.area())
print("Área do retangulo: ", retangulo.area())
print("Área do circulo: ", circulo.area())
print("Área do quadrado: ",quadrado.area())
