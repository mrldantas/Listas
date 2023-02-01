# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, 
# de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes 
# deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do 
# percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

import os


def bytesParaMB(quantosBytes):
    return str(round(quantosBytes / 1048576, 2)).replace('.', ',')


def porcentagem(espacoUsado, total):
    return str(round(espacoUsado * 100 / total, 2)).replace('.', ',')


if (os.path.exists("usuarios.txt")):

    espacosTexto = open("usuarios.txt", "r")
    espacoUsuario = espacosTexto.read().split("\n")

    if len(espacoUsuario) > 0:
        arquivo = open("relatório.txt", "wt")
        arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
        arquivo.write("-" * 72 + "\n")

        arquivo.write("Nr.".ljust(5))
        arquivo.write("Usuário".ljust(15))
        arquivo.write("Espaço utilizado".ljust(21))
        arquivo.write("% do uso".ljust(9) + "\n\n")

        espacoTotal = 0

        for usuarioEspaco in espacoUsuario:
            espacoTotal += int(usuarioEspaco.split()[1])

        for IdxUsuarioEspaco in range(len(espacoUsuario)):
            usuarioEspaco = espacoUsuario[IdxUsuarioEspaco].split()

            usuario = usuarioEspaco[0]
            espaco = usuarioEspaco[1]

            arquivo.write(str(IdxUsuarioEspaco + 1).ljust(5))
            arquivo.write(usuario.ljust(15))
            arquivo.write(bytesParaMB(int(espaco)).rjust(7) + " MB           ")
            arquivo.write(porcentagem(int(espaco), espacoTotal).rjust(7)+"%\n")

        arquivo.write("\nEspaço total ocupado: " + bytesParaMB(espacoTotal) + " MB\n")
        arquivo.write("Espaço médio ocupado: " + bytesParaMB(espacoTotal/len(espacoUsuario)) + " MB")

        arquivo.close()
else:
    print("O arquivo usuarios.txt não existe")
