#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez
frase=input("Digite uma frase: ").strip()
print(f"Quantidade de letras A: {frase.upper().count('A')} \nPosição da primeira aparição: {frase.upper().find('A')+1}\nPosição da última aparação: {frase.upper().rfind('A')+1} ")