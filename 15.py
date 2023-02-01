# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

notas = []
acima = []
abaixo = []

nota = True

while (nota != -1):
    nota = float(input("Insira a nota: "))
    if (nota == -1):
        break
    else:
        notas.append(nota)

print(f"\nValores lidos: {len(notas)}")
print(f"Valores na ordem: {notas}")

notas.reverse()

print(f"Valores na ordem inversa: {notas}")

# Se quiser deixar uma abaixo da outro é só colocar descomentar as linhas abaixo e excluir a de cima:
# for i in range(len(notas)):
    # print(notas[i])

print(f"Soma dos valores: {sum(notas)}")
media = sum(notas) / len(notas)
print(f"Media dos valores: {media}")

for i in range(len(notas)):
    if (notas[i] > media):
        acima.append(notas[i])

print(f"Quantidade de valores a cima da média: {len(acima)}")

for i in range(len(notas)):
    if (notas[i] < 7):
        abaixo.append(notas[i])

print(f"Quantidade de notas a baixo de 7: {len(abaixo)}")
print("ACABOU!")
