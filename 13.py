# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as 
# em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas 
# as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o 
# mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperatura = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i in range(12):
    print(f"\nMês: {meses[i]}")
    temperatura.append(float(input("Insira a temperatura média: ")))

media = sum(temperatura) / 12

for i in range(12):
    if (temperatura[i] > media):
        print(f"\nAcima da média anual: {meses[i]}")
        print(f"Temperatura: {int(temperatura[i])}°")
