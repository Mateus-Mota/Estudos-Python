# Escreva um progama que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
## O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

num_pc=randint(0,5)
num_user=int(input("Advinhe um número entre 0 e 5: "))
if num_user == num_pc:
    print(f"Você venceu! o número correto é {num_pc}")
else:
    print(f"Você perdeu! o número correto é {num_pc}")