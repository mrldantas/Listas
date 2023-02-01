# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos
# pelos elementos intercalados dos dois outros vetores.
# Altere o programa acima, intercalando 3 vetores de 10 elementos cada.

vetorA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetorB = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
vetorC = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
vetorD = []

contador = 0

for i in range(10):
    vetorD.append(vetorA[contador])
    vetorD.append(vetorB[contador])
    vetorD.append(vetorC[contador])

    contador = contador + 1

print(vetorD)
