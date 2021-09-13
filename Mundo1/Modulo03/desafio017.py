#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa
from math import hypot

cat_oposto=int(input("Digite o cateto oposto: "))
cat_adj=int(input("Digite o cateto adjacente: "))
print(f"HIPOTENUSA: {hypot(cat_oposto, cat_adj)}")