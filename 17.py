# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado
# do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um
# programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
# depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
# não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Exercício igual ao 46 da lista de repetição.

saltos = []

nome = True
salto = 1
count = 0

while (nome != ''):
    print("\nPróximo atleta")
    nome = input("Insira o nome do atleta: ")
    if (nome == ''):
        break
    else:
        print("\n")
        for i in range(5):
            print(f"Salto n°{salto}")
            distancia_salto = float(input("Insira a distancia do salto: "))
            saltos.append(distancia_salto)
            salto = salto + 1
        print(f"\nAtleta: {nome}")
        salto = 1
        for i in range(5):
            print(f"{salto}° salto: {saltos[count]}m")
            salto = salto + 1
            count = count + 1
        print(f"\nMelhor salto: {max(saltos)}m")
        print(f"Pior salto: {min(saltos)}m")

        saltos.remove(max(saltos))
        saltos.remove(min(saltos))
        media = sum(saltos) / len(saltos)
        print("\nMedia dos demais saltos: ", round(media, 2))
        print(f"\nResultado Final: \n{nome}: {round(media, 2)}")
