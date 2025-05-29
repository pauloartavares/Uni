"""def criar_tabuleiro_dicionario(linhas, colunas, valor_inicial=' '):
    tabuleiro = {}
    for linha in range(linhas):
        for coluna in range(colunas):
            tabuleiro[(linha, coluna)] = valor_inicial
    return tabuleiro

def imprimir_tabuleiro(tabuleiro, linhas, colunas):
    # Imprimir coordenadas das colunas
    print("   ", end="")  # Espaço para alinhar com os números das linhas (é o espaço antes do nº das colunas)
    for coluna in range(colunas):
        print(f" {coluna} ", end=" ") # Espaço para alinhar os números das colunas
    print("\n  +" + "---+" * colunas)  # Linha separadora inicial, o \n dá a tabulação para fazer a primeira linha separadora
    
    # Imprimir as linhas com números e valores
    for linha in range(linhas):
        print(f"{linha} |", end="")  # Número da linha
        for coluna in range(colunas):
            print(f" {tabuleiro[(linha, coluna)]} |", end="") # alinhas as |
        print("\n  +" + "---+" * colunas)  # Linha separadora entre linhas

# Obter as dimensões do tabuleiro do usuário
linhas = int(input("Introduza o nº de linhas: "))
colunas = int(input("Introduza o nº de colunas: "))

# Criar o tabuleiro
tabuleiro = criar_tabuleiro_dicionario(linhas, colunas)

def atualizar_tabuleiro(tabuleiro, linha, coluna, valor):
    #Atualiza o valor de uma posição específica no tabuleiro.
    if (linha, coluna) in tabuleiro:
        if tabuleiro[(linha, coluna)] == ' ': # se a posição dada estiver vazia então pode atualizar
            tabuleiro[(linha, coluna)] = valor
            return True
        else:
            print("Erro: Essa célula já está ocupada!")
            return False
    else:
        print("Erro: Coordenadas inválidas!")
        return False
    
def verificar_fim(tabuleiro, linhas, colunas):
    #Verifica se o tabuleiro está cheio.
    return all(tabuleiro[(linha, coluna)] != ' ' for linha in range(linhas) for coluna in range(colunas))

# Jogadores e símbolos
jogadores = ["Jogador 1", "Jogador 2"]
simbolos = ["X", "O"]
jogador_atual = 0

# Loop principal do jogo
while not verificar_fim(tabuleiro, linhas, colunas):
    imprimir_tabuleiro(tabuleiro, linhas, colunas)
    print(f"\n{jogadores[jogador_atual]}, é a sua vez!")
    linha = int(input("Informe a linha: "))
    coluna = int(input("Informe a coluna: "))
    
    # Atualiza o tabuleiro se as coordenadas forem válidas
    if atualizar_tabuleiro(tabuleiro, linha, coluna, simbolos[jogador_atual]):
        # Alternar para o próximo jogador
        jogador_atual = 1 - jogador_atual
    else:
        print("Tente novamente!")

# Fim do jogo
imprimir_tabuleiro(tabuleiro, linhas, colunas)
print("O jogo terminou! Todas as células foram preenchidas.")"""

"""import random
jogadores = []

# Lista de cores disponíveis
cores = ["azul", "vermelho", "amarelo", "verde"]
random.shuffle(cores)  # Embaralha as cores aleatoriamente


#Registar jogador
def registar_jogador(matriz, nome):
    if verificar_jogador(matriz, nome) == False:
        cor_atribuida = cores.pop()
        j = {"Nome": nome, "Pontuação": 0, "Cor": cor_atribuida} # dicionário
        matriz.append(j)
        return True
    return False
    
#Verificar se jogador já existe
def verificar_jogador(matriz, nome):
    for jogador in matriz:
         if nome == jogador["Nome"]:    # devemos pesquisar pela chave
             return True
    return False

i = 0
quantos= int(input("Quantos jogadores vão a jogo? (Mínimo de dois jogadores!) "))
if quantos >= 2 and quantos <= 4:
    while i < quantos:
        nome=input("Introduza o nome do jogador: ").lower()
        if registar_jogador(jogadores, nome) == False:
            print ("Esse jogador já existe\n")
        else:
            print("\nJogador adicionado com sucesso\n")
            print("Jogador reconhecido!")
            print(jogadores)
        i += 1"""


"""# Ordena os jogadores de acordo com a cor, começando pelo azul
ordem_jogo = sorted(jogadores, key=lambda x: cores.index(jogadores[x]))"""

"""# Verifica a ordem de jogo
print("Ordem de jogo:")
for jogador in ordem_jogo:
    print(f"{jogador} ({jogadores[jogador]})")"""
