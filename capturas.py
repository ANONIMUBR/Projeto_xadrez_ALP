# Movimento do Rei
def movimento_rei(origem, destino):
    """
    Verifica se o rei pode se movimentar da posição de origem
    até a posição de destino, seguindo as regras do jogo.

    Parâmetros:
        origem: posição inicial do rei no tabuleiro.
        destino: posição para onde o rei deseja se mover.

    Retorno:
        True se o movimento for válido ou False caso contrário.
    """
    if not dentro_tabuleiro(origem) or not dentro_tabuleiro(destino):
        return False

    linha = abs(destino[0] - origem[0])
    coluna = abs(destino[1] - origem[1])

    return (linha <= 1 and coluna <= 1
            and (linha != 0 or coluna != 0))


# Movimento do Cavalo
def movimento_cavalo(origem, destino):
    """
    Verifica se o cavalo está fazendo o movimento em formato de L.

    Parâmetros:
        origem: posição inicial do cavalo no tabuleiro.
        destino: posição para onde o cavalo deseja se mover.

    Retorno:
        True se o movimento for válido ou False caso contrário.
    """
    if not dentro_tabuleiro(origem) or not dentro_tabuleiro(destino):
        return False

    linha = abs(destino[0] - origem[0])
    coluna = abs(destino[1] - origem[1])

    return (linha == 2 and coluna == 1) or (linha == 1 and coluna == 2)


# Verifica se as peças são da mesma cor
def mesma_cor(peca1, peca2):
    """
    Verifica se duas peças pertencem à mesma cor.

    Parâmetros:
        peca1: primeira peça que será comparada.
        peca2: segunda peça que será comparada.

    Retorno:
        True se as peças forem da mesma cor ou False caso contrário.
    """
    if peca1 is None or peca2 is None:
        return False

    cor1 = peca1.split("_")[0]
    cor2 = peca2.split("_")[0]

    return cor1 == cor2


# Verifica se a captura é permitida
def captura_permitida(tabuleiro, origem, destino):
    """
    Verifica se uma peça pode capturar outra no tabuleiro.

    Parâmetros:
        tabuleiro: tabuleiro onde estão as peças.
        origem: posição da peça que fará a captura.
        destino: posição da peça que será capturada.

    Retorno:
        True se a captura puder acontecer ou False caso contrário.
    """
    if not dentro_tabuleiro(origem) or not dentro_tabuleiro(destino):
        return False

    peca_origem = tabuleiro[origem[0]][origem[1]]
    peca_destino = tabuleiro[destino[0]][destino[1]]

    if peca_origem is None or peca_destino is None:
        return False

    if mesma_cor(peca_origem, peca_destino):
        return False

    tipo = peca_origem.split("_")[-1]

    if tipo == "rei":
        return movimento_rei(origem, destino)

    if tipo == "cavalo":
        return movimento_cavalo(origem, destino)

    return False


# Realiza a captura e atualiza o tabuleiro
def capturar_peca(tabuleiro, origem, destino):
    """
    Realiza a captura da peça adversária e atualiza o tabuleiro.

    Parâmetros:
        tabuleiro: tabuleiro onde estão as peças.
        origem: posição da peça que fará a captura.
        destino: posição da peça adversária.

    Retorno:
        True se a captura for realizada ou False se não for permitida.
    """
    if not captura_permitida(tabuleiro, origem, destino):
        return False

    tabuleiro[destino[0]][destino[1]] = tabuleiro[origem[0]][origem[1]]
    tabuleiro[origem[0]][origem[1]] = None

    return True
