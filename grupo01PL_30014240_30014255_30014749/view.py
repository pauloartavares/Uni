from controller import *

import random

def main():
    # Inicialize a variável como uma lista vazia
    matriz_jogadores = []
    while True:
        opcao = input(
            """
            *** MENU ***
            RJ - Registar novo jogador
            IJ - Iniciar Jogo
            MJ - Mostrar Jogadores
            L  - Ler
            G  - Gravar
            VP - Terminar e Visualizar Pontuações
            S  - Sair
            Escolha uma das seguintes opções: """
        ).upper()

        match opcao:
            case "RJ":
                nome = input("Introduza o nome do jogador: ").lower()
                if not registar_jogador(matriz_jogadores, nome):
                    print("Esse jogador já existe\n")
                else:
                    print("\nJogador adicionado com sucesso\n")

            case "MJ":
                if not matriz_jogadores:
                    print("Nenhum jogador registrado.")
                else:
                    print(" Jogadores Registrados\n ")
                    for jogador in matriz_jogadores:
                        print(f"Nome: {jogador['Nome']}, Pontuação: {jogador['Pontuação']}, Peças: {jogador['Peças']}")

            case "IJ":
                if len(matriz_jogadores) >= 2:
                    jogadores = []
                    i = 0
                    simbolos = ["🟦", "🟥", "🟨", "🟩"]
                    cores = ["azul", "vermelho", "amarelo", "verde"]

                    # Configuração dos jogadores
                    quantos = int(input(
                        """
                        Quantos jogadores vão a jogo? 
                        Mín: 2     Máx: 4 
                        """
                    ))
                    cores_disponiveis = cores[:quantos]
                    if 2 <= quantos <= 4:
                        while i < quantos:
                            nome = input(f"Introduza o nome do {i+1}º jogador:\n").lower()
                            if verificar_jogador(matriz_jogadores, nome):
                                jogador = procurar_jogador(matriz_jogadores, nome)
                                if jogador not in jogadores:
                                    jogadores.append(jogador)
                                    print("Jogador reconhecido!")

                                    # Atribuir cor e símbolo ao jogador
                                    while True:
                                        print("\nCores disponíveis:")
                                        print(" ".join(cores_disponiveis))
                                        cor = input("Escolha uma das cores disponíveis:\n").lower()
                                        if cor in cores_disponiveis:
                                            jogador["Cor"] = cor
                                            print(f"A cor {cor} foi atribuída ao {jogador['Nome']}!\n")
                                            cores_disponiveis.remove(cor)
                                            break
                                        else:
                                            print("Cor inválida. Tente novamente.\n")

                                    # Atribuir símbolo e posição na lista de jogadores
                                    indice_cor = cores.index(jogador["Cor"])
                                    jogador["Simbolo"] = simbolos[indice_cor]
                                    if jogador["Cor"] == "azul":
                                        jogadores.remove(jogador)
                                        jogadores.insert(0, jogador)
                                    i += 1
                                else:
                                    print("Esse jogador já está inscrito!")
                            else:
                                print("Jogador não inscrito!")
                    else:
                        print("São necessários pelo menos dois jogadores e no máximo quatro!")


                    # Jogo em equipa ou individual?
                    if quantos == 4:
                        equipas = input("Deseja jogar em equipas? (S/N): ").upper()
                        if equipas == "S":
                            equipas = {
                                "Equipa 1": [],
                                "Equipa 2": []
                            }
                            for jogador in jogadores:
                                if jogador["Cor"] == "azul" or jogador["Cor"] == "vermelho":
                                    equipas["Equipa 1"].append(jogador)
                                else:
                                    equipas["Equipa 2"].append(jogador)
                            print("Equipas formadas:")
                            for equipa, membros in equipas.items():
                                nomes = ", ".join(jogador["Nome"] for jogador in membros)
                                print(f"{equipa}: {nomes}")
                    else:
                        equipas = None

                    # Iniciar o jogo
                    if i == quantos:
                        print("\nJogadores reconhecidos, vamos a jogo!")
                        for jogador in jogadores:
                            jogador["Peças"] -= 1
                        linhas = int(input("Introduza o nº de linhas: "))
                        colunas = int(input("Introduza o nº de colunas: "))
                        print("\n")
                        tabuleiro = criar_tabuleiro_dicionario(linhas, colunas)
                        casas_bonus = adicionar_bonus(linhas, colunas)


                        print(f"O jogador '{jogadores[0]['Nome']}' escolheu a cor Azul e por isso começa o jogo!\n")

                        # Posicionar jogadores no tabuleiro
                        posicoes_iniciais = [
                            (0, 0),
                            (0, colunas - 1),
                            (linhas - 1, colunas - 1),
                            (linhas - 1, 0)
                        ]
                        for idx, jogador in enumerate(jogadores):
                            tabuleiro[posicoes_iniciais[idx]] = jogador["Simbolo"]

                        # Loop principal do jogo
                        jogador_atual = 0
                        while not verificar_fim(tabuleiro, linhas, colunas):
                            imprimir_tabuleiro(tabuleiro, linhas, colunas)
                            jogador = jogadores[jogador_atual]
                            simbolo = jogador["Simbolo"]

                            # Verificar se o jogador tem jogadas possíveis
                            jogadas_possiveis = any(
                                posicao_adjacente(tabuleiro, linha, coluna, simbolo, linhas, colunas) and tabuleiro[(linha, coluna)] == '⬛'
                                for linha in range(linhas)
                                for coluna in range(colunas)
                            )

                            if not jogadas_possiveis:
                                print(f"{jogador['Nome']} não tem jogadas possíveis. Saltando para o próximo jogador.")
                                jogador_atual = (jogador_atual + 1) % len(jogadores)
                                continue

                            # Verificar se o jogador tem peças para jogar
                            if jogador["Peças"] > 0:
                                print(f"\n{jogador['Cor'].upper()} é a sua vez!")
                                print(f"Jogadas restantes: {jogador['Peças']}")
                                validar_linha = False
                                validar_coluna = False
                                while validar_linha == False:
                                    linha = int(input("Informe a linha: "))
                                    if linha > linhas:
                                        print("Linha indicada inválida!")
                                    else:
                                        validar_linha = True
                                while validar_coluna == False:
                                    coluna = int(input("Informe a coluna: "))
                                    if coluna > colunas:
                                        print("Coluna indicada inválida!")
                                    else:
                                        validar_coluna = True
                            else:
                                print(f"Fim de jogo.\n{jogador['Nome']} ficou sem peças.")
                                break

                            # Atualizar o tabuleiro se as coordenadas forem válidas
                            if atualizar_tabuleiro(tabuleiro, linha, coluna, simbolo, linhas, colunas, jogador, jogadores):
                                if (linha, coluna) in casas_bonus:
                                    print(f"O jogador {jogador['Nome']} caiu numa casa com bónus! Joga novamente.")
                                # permite outra jogada
                                    continue    # Salta para a próxima iteração do loop principal do jogo
                                                # ou seja volta ao while sem passar pela atualização do jogador

                                # Alternar para o próximo jogador
                                jogador_atual = (jogador_atual + 1) % len(jogadores)
                                
                            else:
                                print("Jogada inválida. Tente novamente!")

                        # Fim do jogo
                        imprimir_tabuleiro(tabuleiro, linhas, colunas)
                        print("O jogo terminou! Todas as células foram preenchidas.")
                        
                        # Condição para fim de jogo em equipas
                        if isinstance(equipas, dict): # Verifica se equipas é um dicionário 
                            equipa_vencedora (equipas)
                        # Condição para fim de jogo 1 v 1    
                        else:
                            vencedor(jogador, jogadores)
                        
                        #Voltar a colocar as peças a 21 para todos os jogadores
                        for jogador in jogadores:
                            jogador["Peças"] = 21
                else:
                    print("Não existem jogadores para iniciar o jogo!")

            case "L":
                matriz_jogadores = ler_ficheiro_json("data.json")
                if not matriz_jogadores:
                    print("O arquivo 'data.json' está vazio ou inválido. Nenhum jogador foi carregado.")
                else:
                    print("Jogadores carregados do arquivo.")

            case "G":
                escrever_ficheiro_json("data.json", matriz_jogadores)
                print("Jogadores gravados com sucesso.")

            case "VP":
                print("\n Pontuações Finais ")
                for j in matriz_jogadores:
                    print(f"Jogador: {j['Nome']} Pontuação: {j['Pontuação']}")
                print("Parabéns ao vencedor!")

            case "S":
                exit()

            case _:
                print("Opção inválida. Tente novamente.")
