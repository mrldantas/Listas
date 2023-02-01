# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um 
# litro de combustível. Calcule e mostre:
# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros 
# e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. 
# O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

veiculos = ['Corolla', 'Gol', 'UNO', 'Vectra', 'Fusca']
consumo = []

i = 0

for i in range(5):
    print(f"\nVeiculo n°{i + 1} \nNome: {veiculos[i]}")
    km = float(input("Km por litro: "))
    consumo.append(km)

espaco = " "
menorConsumo = consumo.index(max(consumo))

print("\nRelatório final: ")
print(f"{espaco * 4}Carro   Km/L    Litros Necessários        Valor")
print(f"1- {veiculos[0]}  {consumo[0]} {espaco * 10}{round(1000 / consumo[0])} {espaco * 12} R${round(1000 / consumo[0] * 2.25):,.2f}")
print(f"2- {veiculos[1]}  {espaco * 4}{consumo[1]} {espaco * 10}{round(1000 / consumo[1])} {espaco * 12} R${round(1000 / consumo[1] * 2.25):,.2f}")
print(f"3- {veiculos[2]}  {espaco * 4}{consumo[2]} {espaco * 10}{round(1000 / consumo[2])} {espaco * 12} R${round(1000 / consumo[2] * 2.25):,.2f}")
print(f"4- {veiculos[3]}  {espaco * 1}{consumo[3]} {espaco * 10}{round(1000 / consumo[3])} {espaco * 12} R${round(1000 / consumo[3] * 2.25):,.2f}")
print(f"5- {veiculos[4]}  {espaco * 2}{consumo[4]} {espaco * 10}{round(1000 / consumo[4])} {espaco * 12} R${round(1000 / consumo[4] * 2.25):,.2f}")
print("\nO menor consumo é o do ", veiculos[menorConsumo])
