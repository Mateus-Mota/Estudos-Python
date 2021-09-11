#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco=int(input("Preço: "))
print(f"NOVO PREÇO: {preco - ( (preco * 5) / 100 )}")