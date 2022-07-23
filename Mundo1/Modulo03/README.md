# Desafio 016 - Crie um programa que leia um número Real qualquer pelo telcado e mostre na tela a sua posição inteira.
~~~python
from math import floor
num_real=float(input("Digite um número real: "))
print(f"O número inteiro é: {floor(num_real)}")
~~~

# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
~~~python
from math import hypot

cat_oposto=int(input("Digite o cateto oposto: "))
cat_adj=int(input("Digite o cateto adjacente: "))
print(f"HIPOTENUSA: {hypot(cat_oposto, cat_adj)}")
~~~

# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na cossano e tangete de ângulo.
~~~python
from math import sin, cos, tan, radians

angulo=int(input("Digite o ângulo: "))
print(f"SENO: {sin(radians(angulo)):.2f} \nCOSSENO: {cos(radians(angulo)):.2f} \nTANGETE: {tan(radians(angulo)):.2f}")
~~~

# Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
~~~python
from random import choice

alunos = []
for i in range(4):
    alunos.append(input("Digite o nome do aluno: "))
                  
print(choice(alunos))
~~~ 

# Desafio 020 - O mesmo professor do desafio anterior que sortear a ordem de apresentação dos trabalhos alunos. Fala um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
~~~python
from random import shuffle

alunos = []
for i in range(4):
    alunos.append(input("Digite o nome do aluno: "))

shuffle(alunos)
print(alunos)
~~~

# Desafio 021 - Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3
~~~python
import pygame

pygame.mixer.init()
pygame.mixer.music.load('testemp3')
pygame.mixer.music.play()
~~~
