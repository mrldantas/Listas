# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

for i in range(10):
    lista.append(int(input(f"Insira {i + 1}º número : ")))

lista.reverse()

print(lista)
