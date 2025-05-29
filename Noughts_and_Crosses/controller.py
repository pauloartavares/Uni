import json
import random

#Registar jogador
def registar_jogador(matriz, nome):
    if verificar_jogador(matriz, nome) == False:
        j = {"Nome": nome, "Pontuação": 0, "Cor": "", "Peças": 21, "Simbolo": ""} # dicionário
        matriz.append(j)
        return True
    return False
    
#Verificar se jogador já existe
def verificar_jogador(matriz, nome):
    for jogador in matriz:
         if nome == jogador["Nome"]:    # devemos pesquisar pela chave
             return True
    return False

#Escrever no ficheiro
def escrever_ficheiro_json(nome_ficheiro, matriz_jogadores):
    json_string = json.dumps(matriz_jogadores)
    json_file = open (nome_ficheiro, "w")
    json_file.write (json_string)
    json_file.close()

#Ler o ficheiro
def ler_ficheiro_json(nome_ficheiro):
    with open (nome_ficheiro) as f:
        data = json.load(f)
    return data

# Criar tabuleiro
def criar_tabuleiro_dicionario(linhas, colunas, valor_inicial='⬛'):
    tabuleiro = {}
    for linha in range(linhas):
        for coluna in range(colunas):
            tabuleiro[(linha, coluna)] = valor_inicial
    return tabuleiro

def adicionar_bonus(linhas, colunas):
    # Gera uma lista de coordenadas aleatórias
    coordenadas_bonus = set() # o set garante que não existem coordenadas repetidas
    quantidade_bonus = linhas * colunas // 5 # devolve um nº inteiro com base na quantidade de linhas por colunas
    while len(coordenadas_bonus) < quantidade_bonus:
        linha = random.randint(0, linhas - 1) # o randint devolve um nº inteiro. Porquê -1?
        coluna = random.randint(0, colunas - 1) # porque se as linhas/colunas forem 5 ele vai contar do indice 0 ao 4
        coordenadas_bonus.add((linha, coluna))
    return coordenadas_bonus

#Imprimir tabuleiro
def imprimir_tabuleiro(tabuleiro, linhas, colunas):
    # Imprimir coordenadas das colunas
    print("   ", end="")  # Espaço para alinhar com os números das linhas (é o espaço antes do nº das colunas)
    for coluna in range(colunas):
        print(f"  {coluna} ", end=" ") # Espaço para alinhar os números das colunas
    print("\n  +" + "----+" * colunas)  # Linha separadora inicial, o \n dá a tabulação para fazer a primeira linha separadora
    # Imprimir as linhas com números e valores
    for linha in range(linhas):
        print(f"{linha} |", end="")  # Número da linha
        for coluna in range(colunas):
            print(f" {tabuleiro[(linha, coluna)]} |", end="") # alinhas as |
        print("\n  +" + "----+" * colunas)  # Linha separadora entre linhas

# Atualizar tabuleiro
def atualizar_tabuleiro(tabuleiro, linha, coluna, valor, linhas, colunas, jogador, jogadores):
    if jogador["Peças"] > 0:    
        #Atualiza o valor de uma posição específica no tabuleiro.
        if (linha, coluna) in tabuleiro:
            # se a posição dada estiver vazia então pode verificar se é adjacente
            if tabuleiro[(linha, coluna)] == '⬛': 
                # Se a posição for adjacente às outras peças, atualiza
                if posicao_adjacente(tabuleiro, linha, coluna, valor, linhas, colunas):
                    tabuleiro[(linha, coluna)] = valor
                    jogador["Peças"] -= 1
                    for jogador in jogadores:
                        jogador["Pontuação"] = jogador["Peças"]
                    return True
                else:
                    print("Erro: Deve escolher uma célula adjacente às suas!")
                
            else:
                print("Erro: Essa célula já está ocupada!")
                return False
        else:
            print("Erro: Coordenadas inválidas!")
            return False
    else: 
        return False
    
 #Verificar se o tabuleiro está cheio.
def verificar_fim(tabuleiro, linhas, colunas):
    return all(tabuleiro[(linha, coluna)] != '⬛' for linha in range(linhas) for coluna in range(colunas))

def posicao_adjacente(tabuleiro, linha, coluna, simbolo, linhas, colunas):
    #Verifica se a posição desejada é adjacente a uma peça do jogador.
    for i in range(-1, 2): # vai verificar que a linha/coluna nas posições (-1, atual e +1) têm um símbolo igual
        for j in range(-1, 2): # se fosse o intervalo (-1, 1) ele só verificava o (-1 e 0)
            adj_linha = linha + i
            adj_coluna = coluna + j
            if 0 <= adj_linha < linhas and 0 <= adj_coluna < colunas:  # garante que a posição adjacente esteja dentro dos limites do tabuleiro
                if tabuleiro.get((adj_linha, adj_coluna)) == simbolo: # vai buscar o valor naquela posição e comparar com o símbolo a introduzir
                    return True
    return False

def procurar_jogador (jogadores, nome):
    for jogador in jogadores:
        if jogador["Nome"] == nome:
            return jogador
        

def vencedor(jogador, jogadores):
    # Vai encontrar a menor pontuação
    menor_pontuacao = min(jogador["Pontuação"] for jogador in jogadores) # faz o loop em jogadores
    # Vamos filtrar todos os jogadores com a menor pontuação
    # Vai comparar as pontuações de todos os jogadores com a pontuação mínima
    vencedores = []
    for jogador in jogadores:
        if jogador["Pontuação"] == menor_pontuacao:
            vencedores.append(jogador)
    # Exibir resultados
    # Caso haja apenas um vencedor
    if len(vencedores) == 1:
        print(f"O vencedor é {vencedores[0]['Nome']} com {vencedores[0]['Pontuação']} pontos!")
    # Caso haja um empate
    else:
        # Junta os nomes dos vencedores, separados por um  "e"
        nomes = " e ".join(jogador["Nome"] for jogador in vencedores)
        print(f"Há um empate entre {nomes}, todos com {menor_pontuacao} pontos!") 


def atualizar_pontuacao(matriz, jogadores):
    # Atualiza as pontuações
    for jogadores in jogadores:
        nome_jogador = jogadores["Nome"]
        for jogador_matriz in matriz:
            if jogador_matriz["Nome"] == nome_jogador:
                jogador_matriz["Pontuação"] += jogadores["Pontuação"]
                break


def equipa_vencedora (equipas):
    pontuações_equipas = {}
    for equipa, membros in equipas.items():
        pontuação_total = sum(jogador["Peças"] for jogador in membros)
        pontuações_equipas[equipa] = pontuação_total
        print(f"{equipa} tem {pontuação_total} pontos!")
    # Encontra a menor pontuação
    menor_pontuação = min(pontuações_equipas.values())
    # Identifica a(s) equipa(s) com a menor pontuação
    equipas_vencedoras = []
    for equipa, pontuação in pontuações_equipas.items():
        if pontuação == menor_pontuação:
            equipas_vencedoras.append(equipa)
    # Determina o resultado
    if len(equipas_vencedoras) == 1:
        equipa_vencedora = equipas_vencedoras[0]
        print(f"A equipa vencedora é a {equipa_vencedora} com {menor_pontuação} pontos.")
    else:
        print("Houve um empate entre as equipas!")  