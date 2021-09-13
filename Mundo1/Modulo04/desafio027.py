#Faça um programq que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome=input("Digite seu nome completo: ").strip()
print(f"PRIMERO NOME: {nome.split()[0]}\n ÚLTIMO NOME: {nome.split()[len(nome.split())-1]}")