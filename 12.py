# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine 
# quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idade = []
altura = []
aluno13 = []
abaixoMedia = []

for i in range(30):
    print(f"\n{i + 1}º Aluno")
    alturas = altura.append(int(input("Insira a altura (em cm): ")))
    idades = int(input("Insira a idade: "))
    if idades > 13:
        aluno13.append(idades)
    idade.append(idades)

media = sum(altura) / len(altura)

for i in range(len(aluno13)):
    if (aluno13 < media):
        abaixoMedia.append(aluno13)

print(f"Alunos com mais de 13 anos com altura inferior à media é: {len(abaixoMedia)}")
