#Faça um programa que leia um ângulo qualquer e mostre na tela seno, cosseno e tangete de ângulo.

from math import sin, cos, tan, radians

angulo=int(input("Digite o ângulo: "))
print(f"SENO: {sin(radians(angulo)):.2f} \nCOSSENO: {cos(radians(angulo)):.2f} \nTANGETE: {tan(radians(angulo)):.2f}")