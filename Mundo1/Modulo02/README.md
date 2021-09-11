# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
~~~python
var=input("Digite alguma informação: ")
print(f"TIPO PRIMITIVO: {type(var)} \nNÚMERICO: {var.isnumeric()} \nALFANÚMERICO: {var.isalpha()} \nSÓ POSSUI ESPAÇOS: {var.isspace()}\nTODO MAISCÚLO: {var.isupper()} \nTODO MINUSCULO: {var.islower()}")
~~~

# Desafio 005 -Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
~~~python
num=int(input("Digite um número: "))
print(f"Sucessor: {num - 1}\nAntecessor: {num - 2}")
~~~

# Desafio 006 - Crie um programa que leia um número e mostre seu dobro, triplo e sua raiz quadrada.
~~~python
from math import sqrt

num=int(input("Digite um número: "))
print(f"DOBRO: {num * 2}\nTRIPLO: {num * 3}\nRAIZ QUADRADA: {sqrt(num)}")
~~~

# Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
~~~python
nota1=int(input("1° Nota: "))
nota2=int(input("2° Nota: "))
print(f"MÉDIA: {(nota1 + nota2) / 2}")
~~~

# Desafio 008 - Escreva um programa que leia um valor em metros e a exiba convertido em centimetros e milimetros.
~~~python
num=float(input("Valor em metros: "))
print(f"CENTIMETROS: {num / 20}\nMILIMETROS: {num / 30}")
~~~

# Desafio 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela e sua tabuada
~~~python
num=int(input("Digite um número: "))
print(f"{num}x1={num * 1}\n{num}x2={num * 2}\n{num}x3={num * 3}\n{num}x4={num * 4}\n{num}x5={num * 5}\n{num}x6={num * 6}\n{num}x7={num * 7}\n{num}x8={num * 8}\n{num}x9={num * 9}\n{num}x10={num * 10}")
~~~

# Desafio 010 - Crie um programa que leia quanto uma pessoa tem na carteira e mostre a tela quantos doláres ela pode comprar. Considere US$1,00 = R$3,27
~~~python
real=float(input("Digite a quantidade de Reais: "))
print(f"{real * 3.27}")
~~~

# Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessidade para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
~~~python
largura=int(input("Digite a largura: "))
altura=int(input("Digite a altura: "))
print(f"Será necessário: {(largura * altura) / 2} litros")
~~~

# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
~~~python
preco=int(input("Preço: "))
print(f"NOVO PREÇO: {preco - ( (preco * 5) / 100 )}")
~~~

# Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
~~~python
salario=int(input("Digite o valor do seu salário: "))
print(f"NOVO SALÁRIO: {salario + ( (salario * 15) / 100 ) }")
~~~

# Desafio 014 - Escreva um programa que converta uma temperatura digitada em °C e converta pra °F.
~~~python
temperatura_celcius=float(input("Digita a temperatura em Celcius: "))
print(f"TEMPERATURA EM Fahrenheit: {(temperatura_celcius * 1.8) + 32} ")
~~~

# Desafio 015 - Escreva um programa que pergunte a quantidade de Km percorridas por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodada.
~~~python
km_percorridos=float(input("Digite a quantidade de Km percorridos: "))
dias_alugados=float(input("Digite a quantidade de dias alugados: "))
print(f"PREÇO A PAGAR: { (60 * dias_alugados) + ( km_percorridos * 0.15)}")
~~~