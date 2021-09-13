#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
nome=input("Digite o nome completo: ")
print(f"MAIÚSCULO: {nome.upper().strip()} \nMINÚSCULA: {nome.lower().strip()} \nQUANTIDADE DE LETRAS: {len(nome.strip().replace(' ',''))} \nQUANTIDADE DE LETRAS DO 1° NOME: {nome.split()[0]}")