#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario=int(input("Digite o valor do seu salário: "))
print(f"NOVO SALÁRIO: {salario + ( (salario * 15) / 100 ) }")