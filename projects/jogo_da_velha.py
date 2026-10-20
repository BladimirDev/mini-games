import pygame
import sys

# --- CONFIGURACIONES GLOBALES (CONSTANTES) ---
LARGURA, ALTURA = 600, 600
LINHAS, COLUNAS = 3, 3
TAMANHO_QUADRADO = LARGURA // COLUNAS

BRANCO = (255, 255, 255)
CINZA = (200, 200, 200)
VERMELHO = (242, 85, 96)
AZUL = (45, 137, 239)


# --- FUNCIONES DE DIBUJO Y LÓGICA ---
def desenhar_linhas(tela):
    tela.fill(BRANCO)
    for i in range(1, 3):
        # Linhas horizontais
        pygame.draw.line(tela, CINZA, (0, TAMANHO_QUADRADO * i), (LARGURA, TAMANHO_QUADRADO * i), 10)
        # Linhas verticais
        pygame.draw.line(tela, CINZA, (TAMANHO_QUADRADO * i, 0), (TAMANHO_QUADRADO * i, ALTURA), 10)

def desenhar_figuras(tela, tabuleiro):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            centro_x = coluna * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2
            centro_y = linha * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2

            if tabuleiro[linha][coluna] == 1:  # X
                offset = 50
                pygame.draw.line(tela, VERMELHO, (centro_x - offset, centro_y - offset), (centro_x + offset, centro_y + offset), 15)
                pygame.draw.line(tela, VERMELHO, (centro_x - offset, centro_y + offset), (centro_x + offset, centro_y - offset), 15)
            elif tabuleiro[linha][coluna] == 2:  # O
                pygame.draw.circle(tela, AZUL, (centro_x, centro_y), 50, 15)

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador: return True
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador: return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == values e tabuleiro[2][2] == jogador: return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador: return True
    return False

def tabuleiro_cheio(tabuleiro):
    return all(tabuleiro[l][c] != 0 for l in range(LINHAS) for c in range(COLUNAS))


# --- FUNCIÓN PRINCIPAL (MAIN) ---
def main():
    # Inicializa el juego de forma local
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo da Velha - Pygame")
    relogio = pygame.time.Clock()

    # Variables de estado locales (dentro de main)
    tabuleiro = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
    turno_do_x = True
    jogo_ativo = True

    desenhar_linhas(tela)

    # --- LOOP PRINCIPAL ---
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and jogo_ativo:
                mouse_x, mouse_y = evento.pos
                coluna_clicada = mouse_x // TAMANHO_QUADRADO
                linha_clicada = mouse_y // TAMANHO_QUADRADO

                if tabuleiro[linha_clicada][coluna_clicada] == 0:
                    if turno_do_x:
                        tabuleiro[linha_clicada][coluna_clicada] = 1
                        if verificar_vitoria(tabuleiro, 1):
                            pygame.display.set_caption("Jogador X Venceu!")
                            jogo_ativo = False
                        turno_do_x = False
                    else:
                        tabuleiro[linha_clicada][coluna_clicada] = 2
                        if verificar_vitoria(tabuleiro, 2):
                            pygame.display.set_caption("Jogador O Venceu!")
                            jogo_ativo = False
                        turno_do_x = True

                    if jogo_ativo and tabuleiro_cheio(tabuleiro):
                        pygame.display.set_caption("Deu Velha! Empate.")
                        jogo_ativo = False

                    desenhar_figuras(tela, tabuleiro)

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                # Reiniciar el juego limpiando variables locales
                tabuleiro = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
                turno_do_x = True
                jogo_ativo = True
                desenhar_linhas(tela)
                pygame.display.set_caption("Jogo da Velha - Pygame")

        pygame.display.flip()
        relogio.tick(60)

# El punto de entrada seguro de Python
if __name__ == "__main__":
    main()
