def criacao_tabuleiro() -> list:
   tabuleiro = [
      ["T", "C", "B", "Q", "K", "B", "C", "T"],
      ["P", "P", "P", "P", "P", "P", "P", "P"],
      ["", "", "", "", "", "", "", ""],
      ["", "", "", "", "", "", "", ""],
      ["", "", "", "", "", "", "", ""],
      ["", "", "", "", "", "", "", ""],
      ["p", "p", "p", "p", "p", "p", "p", "p"],
      ["t", "c", "b", "q", "k", "b", "c", "t"]
   ]
   return tabuleiro
   
    
def mostrar_tabuleiro(tabuleiro: list):
   """PECAS:
      PRETAS: ♜ ♞ ♝ ♛ ♚ ♟ ██
      BRANCAS: ♖ ♘ ♗ ♕ ♔ ♙ ░░"""

   pecas = {
      "T": "♜ ",
      "t": "♖ ",
      "C": "♞ ",
      "c": "♘ ",
      "B": "♝ ",
      "b": "♗ ",
      "Q": "♛ ",
      "q": "♕ ",
      "K": "♚ ",
      "k": "♔ ",
      "P": "♟ ",
      "p": "♙ ",
      "e_preto": "██",
      "e_branco": "░░"
   }

   print("   1 2 3 4 5 6 7 8\n --------------------")
   
   for i in range(len(tabuleiro)):
      linha = ""
      for j in range(len(tabuleiro[i])):
         if(tabuleiro[i][j]):
            linha += pecas[tabuleiro[i][j]]
         else:
            if(i % 2 == 0):
               linha += pecas["e_branco"] if j % 2 == 0 else pecas["e_preto"]
            else:
               linha += pecas["e_preto"] if j % 2 == 0 else pecas["e_branco"]
      print(f'{i+1}|{linha}')

def posicao_valida(linha_escolhida, coluna_escolhida):
    if 0 < linha_escolhida <= 8 and 0 < coluna_escolhida <= 8:
        return True
    else:
        return False

def mover_peca(origem, destino, tabuleiro):
   linha_origem, coluna_origem = origem
   linha_destino, coluna_destino = destino

   escolha = tabuleiro[linha_origem-1][coluna_origem-1] #lê a posição de origem da peça escolhida
   tabuleiro[linha_destino-1][coluna_destino-1] = escolha #coloca a peça na posição de destino
   tabuleiro[linha_origem-1][coluna_origem-1] = "" #esvazia a casa em que estava a peça antes
