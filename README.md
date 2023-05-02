__Nome__: Lucas Moreira Alves Rodrigues   __RA__: 1840482122014

__Prof. Dr.__ Leandro Luque

## Pratica 04: Orientado a Objeto

### O que temos que fazer? 


* Implemente uma solução capaz de calcular a área de algumas figuras geométricas, como:
    
  * Triangulo: base*altura / 2
    
  * Retangulo: base*altura 
    
  * Circulo: **π** * raio ^2
    
  Escreva um programa principal também e represente as classes com UML.
***
### Resolução da pratica 04: 
* Aqui é a parte do código que o Professor pediu:
    * Fiz Utilizando Linguagem de Programação Python, pois tenho mais facilidade com ela.
```
print('Coloca aqui o código')
```
Fiz algumas modificações no código, além de colocar o cálculo do triângulo, retângulo e circulo achei interessante colocar o cálculo do quadrado também. Queria colocar outras formas geométricas como losango ou trapézio, só que eu teria que importa mais uma biblioteca e o código iria ficar muito grande.

### Representação das classes com UML
![a80138c0](https://user-images.githubusercontent.com/112831891/235556492-82ef5550-dabe-49a2-8ab9-e28988236123.jpg)

As classes, Triangulo, Retângulo, Circulo e Quadrado herdam a classe abstrata FiguraGeometrica e implementam o método area().

