# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números
# pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista = []
impar = []
par = []

count = 0

for i in range(4):
    lista.append(int(input(f"Insira o {i + 1} número: ")))
    if (lista[count] % 2 == 0):
        par.append(lista[count])
    else:
        impar.append(lista[count])
    count = count + 1

print(f"\nNúmeros inseridos: {lista}")
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")
