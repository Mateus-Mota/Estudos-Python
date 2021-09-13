#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
numeros=int(input("Digite um número entre 0 e 9999: "))
num=str(numeros)
print(f"MILHAR: {num[0]}\nCENTENA: {num[1]}\nDEZENA: {num[2]}\nUNIDADE: {num[3]}")
