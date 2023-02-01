# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

from functools import reduce
from operator import mul

lista = []
produto = 1

for i in range(5):
    numero = lista.append(int(input(f"Insira o {i + 1}º número: ")))

produto = reduce(mul, lista, 1)

print(f"Os números são: {lista}")
print(f"A soma é igual a: {sum(lista)}")
print(f"O produto é igual a: {produto}")
