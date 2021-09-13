#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice

alunos = []
for i in range(4):
    alunos.append(input("Digite o nome do aluno: "))
                  
print(choice(alunos))
