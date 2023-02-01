# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?: ", "Esteve no local do crime?: ", "Mora perto da vítima?: ", "Devia para a vítima?: ", "Já trabalhou com a vítima?: "]

sim = 0

for i in range(len(perguntas)):
    resposta = input(perguntas[i])
    if (resposta == 'sim'):
        sim = sim + 1

if (sim == 2):
    print("\nSuspeita!")
elif (sim > 2 and sim <= 4):
    print("\nCúmplice!")
elif (sim == 5):
    print("\nAssassino!")
else:
    print("\nInocente!")
