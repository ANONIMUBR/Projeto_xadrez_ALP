import tabuleiro
import pecas_linha

# Movimento do Rei
def movimento_rei(origem, destino, tab):
    """
    Valida e executa o movimento (e eventual captura) do rei no tabuleiro.

    Parâmetros:
        origem: posição inicial do rei no tabuleiro (linha, coluna).
        destino: posição para onde o rei deseja se mover (linha, coluna).
        tab: tabuleiro onde estão as peças.

    Retorno:
        True se o movimento for realizado ou False caso contrário.
    """
    if not (tabuleiro.posicao_valida(origem[0], origem[1]) and tabuleiro.posicao_valida(destino[0], destino[1])):
        return False

    linha = abs(destino[0] - origem[0])
    coluna = abs(destino[1] - origem[1])

    if (linha <= 1 and coluna <= 1 and (linha != 0 or coluna != 0)
            and pecas_linha.caminho_livre(origem[0], origem[1], destino[0], destino[1], tab)):
        if tab[destino[0]-1][destino[1]-1]:
            if not captura_permitida(origem, destino, tab):
                return False
            capturar_peca(origem, destino, tab)

        tabuleiro.mover_peca(origem, destino, tab)
        return True

    return False

# Movimento do Cavalo
def movimento_cavalo(origem, destino, tab):
    """
    Valida e executa o movimento em L (e eventual captura) do cavalo no tabuleiro.

    Parâmetros:
        origem: posição inicial do cavalo no tabuleiro (linha, coluna).
        destino: posição para onde o cavalo deseja se mover (linha, coluna).
        tab: tabuleiro onde estão as peças.

    Retorno:
        True se o movimento for realizado ou False caso contrário.
    """
    if not (tabuleiro.posicao_valida(origem[0], origem[1]) and tabuleiro.posicao_valida(destino[0], destino[1])):
        return False

    linha = abs(destino[0] - origem[0])
    coluna = abs(destino[1] - origem[1])

    if (linha == 2 and coluna == 1) or (linha == 1 and coluna == 2):
        if tab[destino[0]-1][destino[1]-1]:
            if not captura_permitida(origem, destino, tab):
                return False
            capturar_peca(origem, destino, tab)

        tabuleiro.mover_peca(origem, destino, tab)
        return True

    return False

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
    if not peca1 or not peca2:
        return False

    cor1 = "p" if peca1 == peca1.upper() else "b"
    cor2 = "p" if peca2 == peca2.upper() else "b"

    return cor1 == cor2


# Verifica se a captura é permitida
def captura_permitida(origem, destino, tab):
    """
    Verifica se uma peça pode capturar outra no tabuleiro.

    Parâmetros:
        origem: posição da peça que fará a captura.
        destino: posição da peça que será capturada.
        tab: tabuleiro onde estão as peças.

    Retorno:
        True se a captura puder acontecer ou False caso contrário.
    """
    if not (tabuleiro.posicao_valida(origem[0], origem[1]) and tabuleiro.posicao_valida(destino[0], destino[1])):
        return False

    peca_origem = tab[origem[0]-1][origem[1]-1]
    peca_destino = tab[destino[0]-1][destino[1]-1]

    if not peca_origem or not peca_destino:
        return False

    return not mesma_cor(peca_origem, peca_destino)


# Realiza a captura (remove a peça adversária do destino)
def capturar_peca(origem, destino, tab):
    """
    Remove a peça adversária do destino no tabuleiro, mantendo o mesmo
    comportamento de captura_peca do Código 2.

    Parâmetros:
        origem: posição da peça que fará a captura.
        destino: posição da peça adversária.
        tab: tabuleiro onde estão as peças.

    Retorno:
        True se a captura for realizada ou False se as posições forem inválidas.
    """
    if not (tabuleiro.posicao_valida(origem[0], origem[1]) and tabuleiro.posicao_valida(destino[0], destino[1])):
        return False
    tab[destino[0]-1][destino[1]-1] = ""
    return True
