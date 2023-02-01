# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(4):
    notas.append(float(input(f"Insira a {i + 1}º nota: ")))

media = sum(notas) / 4

print(f"\nNotas: {notas}")
print(f"\nA média é: {media}")
