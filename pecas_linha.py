import tabuleiro
import capturas

def movimento_torre(linha_origem: int, coluna_origem: int, linha_destino: int, coluna_destino: int, tab: list) -> bool:
    delta_l = abs(linha_destino - linha_origem)
    delta_c = abs(coluna_destino - coluna_origem)

    if (tabuleiro.posicao_valida(linha_origem, coluna_origem)
        and tabuleiro.posicao_valida(linha_destino, coluna_destino)
        and ((delta_l == 0 and delta_c > 0) or (delta_c == 0 and delta_l > 0))
        and caminho_livre(linha_origem, coluna_origem, linha_destino, coluna_destino, tab)):

        origem = (linha_origem, coluna_origem)
        destino = (linha_destino, coluna_destino)

        if tab[linha_destino][coluna_destino] != "":
            if not capturas.captura_permitida(tab, origem, destino):
                return False
            capturas.capturar_peca(tab, origem, destino)
        else:
            tabuleiro.mover_peca(tab, origem, destino)

        return True

    return False

def movimento_bispo(linha_origem: int, coluna_origem: int, linha_destino: int, coluna_destino: int, tab: list) -> bool:
    delta_l = abs(linha_destino - linha_origem)
    delta_c = abs(coluna_destino - coluna_origem)

    if (tabuleiro.posicao_valida(linha_origem, coluna_origem)
        and tabuleiro.posicao_valida(linha_destino, coluna_destino)
        and delta_l == delta_c and delta_l > 0
        and caminho_livre(linha_origem, coluna_origem, linha_destino, coluna_destino, tab)):

        origem = (linha_origem, coluna_origem)
        destino = (linha_destino, coluna_destino)

        if tab[linha_destino][coluna_destino] != "":
            if not capturas.captura_permitida(tab, origem, destino):
                return False
            capturas.capturar_peca(tab, origem, destino)
        else:
            tabuleiro.mover_peca(tab, origem, destino)

        return True

    return False

def movimento_dama(linha_origem: int, coluna_origem: int, linha_destino: int, coluna_destino: int, tab: list) -> bool:
    delta_l = abs(linha_destino - linha_origem)
    delta_c = abs(coluna_destino - coluna_origem)

    if (tabuleiro.posicao_valida(linha_origem, coluna_origem)
        and tabuleiro.posicao_valida(linha_destino, coluna_destino)
        and ((delta_l == 0 and delta_c > 0)
        or (delta_c == 0 and delta_l > 0)
        or (delta_l == delta_c and delta_l > 0))
        and caminho_livre(linha_origem, coluna_origem, linha_destino, coluna_destino, tab)):

        origem = (linha_origem, coluna_origem)
        destino = (linha_destino, coluna_destino)

        if tab[linha_destino][coluna_destino] != "":
            if not capturas.captura_permitida(tab, origem, destino):
                return False
            capturas.capturar_peca(tab, origem, destino)
        else:
            tabuleiro.mover_peca(tab, origem, destino)

        return True

    return False

def caminho_livre(linha_origem: int, coluna_origem: int, linha_destino: int, coluna_destino: int, tab: list) -> bool:
    passo_l = (linha_destino > linha_origem) - (linha_destino < linha_origem)
    passo_c = (coluna_destino > coluna_origem) - (coluna_destino < coluna_origem)

    linha, coluna = linha_origem + passo_l, coluna_origem + passo_c

    while (linha, coluna) != (linha_destino, coluna_destino):
        if tab[linha][coluna] != "":
            return False
        linha += passo_l
        coluna += passo_c

    return True

