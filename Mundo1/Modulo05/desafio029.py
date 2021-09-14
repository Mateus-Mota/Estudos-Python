#Escreve um programa que leia a velocidade de um carro.
#Se ele ultrapssar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 por cada Km acima do limite.
velocidade_carro=int(input("Digite a velocidade do carro: "))
if velocidade_carro > 80:
    print(f"VELOCIDADE LIMITE IGUAL A 80KM/h, VOCÊ SERÁ MULTADO NO VALOR DE {(velocidade_carro - 80) * 7} R$ POIS ESTAVA A {velocidade_carro} Km/h")
else:
    print(f"Você não ultrapassou o limite de velocidade!")