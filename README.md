# Pratica 04: Orientado a Objeto

### O que temos que fazer? 


* Implemente uma solução capaz de calcular a área de algumas figuras geométricas, como:
    
  * Triangulo: base*altura / 2
    
  * Retangulo: base*altura 
    
  * Circulo: **π** * raio ^2
    
  Escreva um programa principal também e represente as classes com UML.
***
### A minha resolução: 
* Aqui é a parte do código que o Professor pediu:
```
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
    
triangulo = Triangulo()
retangulo = Retangulo()
circulo = Circulo()

print('Área do triangulo: ', triangulo.area())
print("Área do retangulo: ", retangulo.area())
print("Área do circulo: ", circulo.area())
```
Fiz algumas modificações no código, além de colocar o calculo do traingulo, reatngulo e circulo achei interessante colocar o calculo de outras figuras geometricas como:quadrado, losango, trapézio.
 
