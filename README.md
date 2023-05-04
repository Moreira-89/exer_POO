__Nome__: Lucas M. A. Rodrigues

__Prof. Dr.__ Leandro Luque

## Prática 04: Orientado a Objeto

### O que temos que fazer? 


* Implemente uma solução capaz de calcular a área de algumas figuras geométricas, como:
    
  * Triangulo: base*altura / 2
    
  * Retangulo: base*altura 
    
  * Circulo: **π** * raio ^2
    
  Escreva um programa principal também e represente as classes com UML.
***
### Resolução da prática 04: 
Seguindo o que foi pedido pelo professor, decidir fazer todo o meu código utilizando a linguagem de programação Python, pois tenho mais facilidade.  Aqui está o código: 

__Programa Principal (poo.py)__
```
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
```
__Classe Triangulo (triangulo.py)__
```
class Triangulo:
    def area(self):
        base = float(input("Digite a base do Triangulo: "))
        altura = float(input("Digite a altura do Triangulo: "))
        return (base * altura) / 2
```
__Classe Quadrado (quadrado.py)__
```
class Quadrado:
    def area(self):
        lado = float(input("Digite o lado do quadrado: "))
        return lado ** 2
```
__Classe Retangulo (retangulo.py)__
```
class Retangulo:
    def area(self):
        base = float(input("Digite a base do Retangulo: "))
        altura = float(input("Digite a altura do Retangulo: "))
        return base * altura
```
__Classe Circulo (circulo.py)__
```
import math
class Circulo:
    def area(self):
        raio = float(input("Digite o raio do Circulo: "))
        return math.pi * (raio ** 2)
```
Seguindo as boas práticas de programação dentro de POO, eu fiz um arquivo para cada classe e depois juntei em um arquivo só utilizando o __import__ do Python.
***
### Representação das classes com UML
![a80138c0](https://user-images.githubusercontent.com/112831891/235556492-82ef5550-dabe-49a2-8ab9-e28988236123.jpg)

As classes, Triangulo, Retângulo, Circulo e Quadrado herdam a classe abstrata FiguraGeometrica e implementam o método area().

