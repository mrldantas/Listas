# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

salarios = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699], [700, 799], [800, 899], [900, 999]]
quantidades = [0, 0, 0, 0, 0, 0, 0, 0, 0]

vendas = True

while (vendas != 0):
    vendas = float(input("Insira o quanto foi vendido: "))
    if (vendas == 0):
        break
    else:
        salario = (vendas * 0.09) + 200
        if (salario < 1000):
            for i in range(len(salarios)):
                if ((salario > salarios[i][0]) and (salario < salarios[i][1])):
                    quantidades[i] += 1
        else:
            quantidades[8] += 1

for i in range(len(salarios)):
    print(f"Entre R${salarios[i][0]} e R${salarios[i][1]}: {quantidades[i]}")

print(f"Salários maiores que R$1000: {quantidades[8]}")
