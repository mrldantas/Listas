# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro 
# vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
# intercalados dos dois outros vetores.

vetorA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetorB = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
vetorC = []

contador = 0

for i in range(10):
    vetorC.append(vetorA[contador])
    vetorC.append(vetorB[contador])

    contador = contador + 1

print(vetorC)
