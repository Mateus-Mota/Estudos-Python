#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
var=input("Digite alguma informação: ")
print(f"TIPO PRIMITIVO: {type(var)} \nNÚMERICO: {var.isnumeric()} \nALFANÚMERICO: {var.isalpha()} \nSÓ POSSUI ESPAÇOS: {var.isspace()}\nTODO MAISCÚLO: {var.isupper()} \nTODO MINUSCULO: {var.islower()}")