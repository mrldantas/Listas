# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
# O total de votos computados;
# Os númeos e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

votos = []
jogadoresVotados = []
numerosJogadores = []

voto = True
numeroVoto = 1

print("Enquete: Quem foi o melhor jogador?")

while (voto != 0):
    print(f"\nVoto n°{numeroVoto}")
    voto = int(input("Insira o número do jogador: "))
    if (voto == 0):
        break
    else:
        while ((voto > 23) or (voto < 1)):
            print("[Voto inválido.]")
            print(f"Voto n°{numeroVoto}")
            voto = int(input("Insira o número novamente: "))
        votos.append(voto)
    numeroVoto = numeroVoto + 1

print("\nResultado da votação: ")
print(f"\nTotal de votos: {len(votos)}")
count = 1

for i in range(23):
    if count not in votos:
        count = count + 1
        continue
    else:
        jogadoresVotados.append(votos.count(count))
        numerosJogadores.append(count)
        print(f"\nVotos para o jogador camisa n°{count} = {votos.count(count)}")
        print(f"Percentual de votos: {round(100 * votos.count(count) / len(votos))}%")
        count = count + 1

melhor = jogadoresVotados.index(max(jogadoresVotados))

print(f"\nO jogador vencedor foi o n°{numerosJogadores[melhor]} com {jogadoresVotados[melhor]} votos")
print(f"Ganhou com {round(100 * jogadoresVotados[melhor] / len(votos))}% dos votos")
