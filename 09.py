# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e
# mostre a soma dos quadrados dos elementos do vetor.

vetor = []
soma = 0

for i in range(10):
    vetor.append(int(input(f"Insira o {i + 1}º número: ")))
    soma = soma + (vetor[len(vetor)-1]**2)
print(f"A soma dos quadrados dos elementos do vetor é: {soma}")
