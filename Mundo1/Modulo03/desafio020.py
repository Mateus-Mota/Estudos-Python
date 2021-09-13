#O mesmo professor do desafio anterior que sortear a ordem de apresentação dos trabalhos alunos. 
#Fala um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

alunos = []
for i in range(4):
    alunos.append(input("Digite o nome do aluno: "))

shuffle(alunos)
print(alunos)