#Crie um programa que leia um número e mostre seu dobro, triplo e sua raiz quadrada.
from math import sqrt

num=int(input("Digite um número: "))
print(f"DOBRO: {num * 2}\nTRIPLO: {num * 3}\nRAIZ QUADRADA: {sqrt(num)}")