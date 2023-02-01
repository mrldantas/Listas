# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

defeitos = ["Necessita da Esfera", "Necessita de Limpeza", "Necessita Troca do Cabo", "Quebrado ou Inutilizado"]
identificacao = []
numeroDefeitos = []

numero = True
mouse = 1

while (numero != 0):
    print(f"\nMouse n°{mouse}")
    numero = int(input("Insira o número de identificação do mouse: "))
    if (numero == 0):
        break
    else:
        while (numero in identificacao):
            print(f"\nMouse n°{mouse}")
            numero = int(input("Insira o número de identificação do mouse: "))
        numeroDefeito = int(input("Insira o número do defeito: "))
        while ((numeroDefeito > 4) or (numeroDefeito < 1)):
            numeroDefeito = int(input("Insira novamente o número do defeito: "))
        identificacao.append(numero)
        numeroDefeitos.append(numeroDefeito)
    mouse = mouse + 1


espaco = " "

print(f"\nQuantidade de mouses: {len(identificacao)}")
print("\n       Situação        Quantidade        Percentual")
print(f"{defeitos[0]} {espaco * 6} {numeroDefeitos.count(0 + 1)} {espaco * 13} {round(100 * numeroDefeitos.count(0 + 1) / len(identificacao))}%")
print(f"{defeitos[1]} {espaco * 5} {numeroDefeitos.count(1 + 1)} {espaco * 13} {round(100 * numeroDefeitos.count(1 + 1) / len(identificacao))}%")
print(f"{defeitos[2]} {espaco * 2} {numeroDefeitos.count(2 + 1)} {espaco * 13} {round(100 * numeroDefeitos.count(2 + 1) / len(identificacao))}%")
print(f"{defeitos[3]} {espaco * 2} {numeroDefeitos.count(3 + 1)} {espaco * 13} {round(100 * numeroDefeitos.count(3 + 1) / len(identificacao))}%")
