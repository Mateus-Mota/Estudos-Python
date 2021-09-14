#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0,45 para vigens mais longas.
distancia_km=int(input("Digite a a distância da viagem em Km/h: "))
if distancia_km < 200:
    print(f"PREÇO DA VIAGEM: {(distancia_km * 0.50):.2f} R$")
else:
    print(f"PREÇO DA VIAGEM: {(distancia_km * 0.45):.2f} R$")