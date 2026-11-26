import capturas
import tabuleiro
import pecas_linha
def movimento_peao(origem, destino, tab: list) -> bool:
   x1, y1 = origem
   x2, y2 = destino
   
   if not (tabuleiro.posicao_valida(x1, y1) and tabuleiro.posicao_valida(x2, y2)):
      return False

   cor = "p" if tab[x1-1][y1-1] == tab[x1-1][y1-1].upper() else "b"
   direcao = 1 if cor == "p" else -1
   linha_inicial = 2 if cor == "p" else 7
   dx = x2 - x1
   dy = abs(y2 - y1)
   alvo = tab[x2-1][y2-1]

   if dy == 0 and not alvo:
      if dx == direcao or (dx == 2 * direcao and x1 == linha_inicial
                           and pecas_linha.caminho_livre((x1, y1), (x2, y2), tab)):
         tabuleiro.mover_peca((x1, y1), (x2, y2), tab)
         return True

   elif dy == 1 and dx == direcao and alvo and capturas.captura_permitida((x1, y1), (x2, y2), tab):
      capturas.capturar_peca(origem, destino, tab)
      tabuleiro.mover_peca(origem, destino, tab)
      return True
   return False


def executa_movimento(origem, destino, tab):
   # movimentos = {
   #    "t": pecas_linha.movimento_torre,
   #    "c": capturas.movimento_cavalo,
   #    "b": pecas_linha.movimento_bispo,
   #    "q": pecas_linha.movimento_dama,
   #    "k": capturas.movimento_rei,
   #    "p": peao.movimento_peao,
   # }
   x1, y1 = origem
   x2, y2 = destino

   peca = tab[x1-1][y1-1].lower()
   match peca:
      case "t":
         result = pecas_linha.movimento_torre(origem, destino, tab)
      case "c":
         result = capturas.movimento_cavalo(origem, destino, tab)
      case "b":
         result = pecas_linha.movimento_bispo(origem, destino, tab)
      case "q":
         result = pecas_linha.movimento_dama(origem, destino, tab)
      case "k":
         result = capturas.movimento_rei(origem, destino, tab)
      case "p":
         result = movimento_peao(origem, destino, tab)
      case _:
         result = False

   return result


def controlar_turno(origem, tab: list, turno: str) -> bool:
   x1, y1 = origem
   if not tabuleiro.posicao_valida(x1, y1):
      return False
   peca = tab[x1-1][y1-1]
   turno_mod = turno.upper() if turno == "p" else turno.lower()
   return bool(peca) and capturas.mesma_cor(peca, turno_mod)


def trocar_turno(turno: str) -> str:
   return "b" if turno == "p" else "p"
