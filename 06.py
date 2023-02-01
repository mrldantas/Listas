# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor
# a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

acimaMedia = []

for i in range(2):
    notas = []
    print(f"\n{i + 1}º Aluno")
    for i in range(4):
        nota = int(input("Insira sua nota [0 a 10]: "))
        notas.append(nota)
        while ((nota > 10) or (nota < 0)):
            nota = int(input("Insira sua nota novamente [0 a 10]: "))
            notas.append(nota)
    media = sum(notas) / len(notas)
    if (media >= 7):
        acimaMedia.append(media)

print(f"\nAlunos com média maior que 7: {len(acimaMedia)}")
