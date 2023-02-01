# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao
# final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0,
# que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido
# completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e
# informar o vencedor da enquete.

votos = []
numeroVotos = []
opcoes = ['Windowns Server', 'Unix', 'Linux', 'NetWare', 'MacOS', 'Outro']

voto = True
numeroVoto = 1

i = 0

print("\nQual o melhor Sistema Operacional para uso em servidores?")

print("\nAs possíveis respostas são:")

print("\n1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- Mac OS")
print("6- Outro")

while (voto != 0):
    print(f"\nVoto n°{numeroVoto}")
    voto = int(input("Insira o seu voto: "))
    if (voto == 0):
        break
    else:
        while ((voto > 6) or (voto < 1)):
            print("[Voto invalido]")
            print(f"\nVoto n°{numeroVoto}")
            voto = int(input("Insira seu voto novamente: "))
        votos.append(voto)
    numeroVoto = numeroVoto + 1

printSistema = ("Sistema Operacional")
espaco = " "

printVotos = "Votos"

print("\nSistema Operacional | Votos |    %    |")
print("---------------------------------------")

numeroVotos.append(votos.count(i + 1))

print(f"{opcoes[0]} {espaco * 7} {votos.count(0 + 1)} {espaco * 4} {round(100 * votos.count(0 + 1) / len(votos), 2)}%")
print(f"{opcoes[1]} {espaco * 18} {votos.count(1 + 1)} {espaco * 4} {round(100 * votos.count(1 + 1) / len(votos), 2)}%")
print(f"{opcoes[2]} {espaco * 17} {votos.count(2 + 1)} {espaco * 4} {round(100 * votos.count(2 + 1) / len(votos), 2)}%")
print(f"{opcoes[3]} {espaco * 15} {votos.count(3 + 1)} {espaco * 4} {round(100 * votos.count(3 + 1) / len(votos), 2)}%")
print(f"{opcoes[4]} {espaco * 17} {votos.count(4 + 1)} {espaco * 4} {round(100 * votos.count(4 + 1) / len(votos), 2)}%")
print(f"{opcoes[5]} {espaco * 17} {votos.count(5 + 1)} {espaco * 4} {round(100 * votos.count(5 + 1) / len(votos), 2)}%")
print("---------------------------------------")
print(f"Total {espaco * 16} {len(votos)}")

ganhador = numeroVotos.index(max(numeroVotos))

print(f"\nO sistema mais votado foi o, {opcoes[ganhador]}, com {numeroVotos[ganhador]} votos, correspondendo a {round(100 * numeroVotos[ganhador] / len(votos), 2)}% dos votos.")
