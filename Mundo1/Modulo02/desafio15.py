#Escreva um programa que pergunte a quantidade de Km percorridas por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodada.
km_percorridos=float(input("Digite a quantidade de Km percorridos: "))
dias_alugados=float(input("Digite a quantidade de dias alugados: "))
print(f"PREÇO A PAGAR: { (60 * dias_alugados) + ( km_percorridos * 0.15)}")