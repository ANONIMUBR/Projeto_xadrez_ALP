import tabuleiro
import capturas

def movimento_torre(origem:list, destino:list, tab: list) -> bool:
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino
    
    delta_l = abs(linha_destino - linha_origem)
    delta_c = abs(coluna_destino - coluna_origem)

    if (tabuleiro.posicao_valida(linha_origem, coluna_origem)
        and tabuleiro.posicao_valida(linha_destino, coluna_destino)
        and ((delta_l == 0 and delta_c > 0) or (delta_c == 0 and delta_l > 0))
        and caminho_livre(origem, destino, tab)):

        if tab[linha_destino-1][coluna_destino-1] != "":
            if not capturas.captura_permitida(origem, destino, tab):
                return False
            capturas.capturar_peca(origem, destino, tab)
        else:
            tabuleiro.mover_peca(origem, destino, tab)

        return True

    return False

def movimento_bispo(origem:list, destino:list, tab: list) -> bool:
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino
    
    delta_l = abs(linha_destino - linha_origem)
    delta_c = abs(coluna_destino - coluna_origem)

    if (tabuleiro.posicao_valida(linha_origem, coluna_origem)
        and tabuleiro.posicao_valida(linha_destino, coluna_destino)
        and delta_l == delta_c and delta_l > 0
        and caminho_livre(origem, destino, tab)):

        if tab[linha_destino-1][coluna_destino-1] != "":
            if not capturas.captura_permitida(origem, destino, tab):
                return False
            capturas.capturar_peca(origem, destino, tab)
        else:
            tabuleiro.mover_peca(origem, destino, tab)

        return True

    return False

def movimento_dama(origem:list, destino:list, tab: list) -> bool:
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino
    
    delta_l = abs(linha_destino - linha_origem)
    delta_c = abs(coluna_destino - coluna_origem)

    if (tabuleiro.posicao_valida(linha_origem, coluna_origem)
        and tabuleiro.posicao_valida(linha_destino, coluna_destino)
        and ((delta_l == 0 and delta_c > 0)
        or (delta_c == 0 and delta_l > 0)
        or (delta_l == delta_c and delta_l > 0))
        and caminho_livre(origem, destino, tab)):

        if tab[linha_destino-1][coluna_destino-1] != "":
            if not capturas.captura_permitida(origem, destino, tab):
                return False
            capturas.capturar_peca(origem, destino, tab)
        else:
            tabuleiro.mover_peca(origem, destino, tab)

        return True

    return False

def caminho_livre(origem:list, destino:list, tab: list) -> bool:
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    passo_l = (linha_destino > linha_origem) - (linha_destino < linha_origem)
    passo_c = (coluna_destino > coluna_origem) - (coluna_destino < coluna_origem)

    linha, coluna = linha_origem + passo_l, coluna_origem + passo_c

    while (linha, coluna) != (linha_destino, coluna_destino):
        if tab[linha-1][coluna-1] != "":
            return False
        linha += passo_l
        coluna += passo_c

    return True

