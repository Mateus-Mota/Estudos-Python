#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para salários inferiores ou iguais, o aumento é de 15%.
salario=float(input("Digite o salário: "))
if salario > 1250.00:
    print(f"NOVO SALÁRIO: {((salario * 10) / 100 ) + salario}")
else:
    print(f"NOVO SALÁRIO: {((salario * 15) / 100) + salario}")