# Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
## O nome com todas as letras maiúsculas
## O nome com todas minúsculas.
## Quantas letras ao todo (sem considerar espaços).
## Quantas letras tem o primeiro nome.
~~~python
nome=input("Digite o nome completo: ")
print(f"MAIÚSCULO: {nome.upper().strip()} \nMINÚSCULA: {nome.lower().strip()} \nQUANTIDADE DE LETRAS: {len(nome.strip().replace(' ',''))} \nQUANTIDADE DE LETRAS DO 1° NOME: {nome.split()[0]}")
~~~
 
# Desafio 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
~~~python
numeros=int(input("Digite um número entre 0 e 9999: "))
num=str(numeros)
print(f"MILHAR: {num[0]}\nCENTENA: {num[1]}\nDEZENA: {num[2]}\nUNIDADE: {num[3]}")
~~~ 

# Desafio 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
~~~python
cidade=input("Digite o nome de uma cidade: ")
print(cidade.split()[0].upper() == "SANTO")
~~~ 

# Desafio 025 - Crie um programa que leia o nome de uma pesssoa e diga se ela tem "SILVA" no nome.
~~~python
nome=input("Digite um nome: ").strip()
print(f"{'SILVA' in nome.upper()}")
~~~ 

# Faça um programa que leia uma frase pelo teclado e mostre:
## Quantas vezes aparece a letra "A"
## Em que posição ela aparece a primeira vez
## Em que posição ela aparece a última vez
~~~python
frase=input("Digite uma frase: ").strip()
print(f"Quantidade de letras A: {frase.upper().count('A')} \nPosição da primeira aparição: {frase.upper().find('A')+1}\nPosição da última aparação: {frase.upper().rfind('A')+1} ")
~~~ 


# Faça um programq que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
~~~python
nome=input("Digite seu nome completo: ").strip()
print(f"PRIMERO NOME: {nome.split()[0]}\n ÚLTIMO NOME: {nome.split()[len(nome.split())-1]}")
~~~ 