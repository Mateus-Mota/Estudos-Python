#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1=int(input("Digite um 1° número: "))
num2=int(input("Digite o 2° número: "))
num3=int(input("Digite o 3° número: "))

if num1 > num2 and num2 > num3:
    print(f"MAIOR: {num1}\nMENOR: {num3}")

elif num1 > num2 and num3 > num2:
    print(f"MAIOR: {num1}\nMENOR: {num2}")

elif num2 > num1 and num1 > num3:
    print(f"MAIOR: {num2}\nMENOR: {num3}")

elif num2 > num3 and num3 > num1:
    print(f"MAIOR: {num2}\nMENOR: {num1}")

elif num3 > num1 and num1 > num2:
    print(f"MAIOR: {num3}\nMENOR: {num2}")

else:
    print(f"MAIOR: {num3}\nMENOR: {num1}")
