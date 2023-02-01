# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = []
contador = 0

for i in range(10):
    lista.append(input(f"Insira o {i + 1}º caractere: "))
    caractere = lista[i]
    if (caractere not in ('a', 'e', 'i', 'o', 'u')):
        contador = contador + 1

print(f"Foram inseridos {contador} consoantes")
