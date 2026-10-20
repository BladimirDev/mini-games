import pygame
import sys

# 1. Inicialização e Configurações Base
pygame.init()

LARGURA, ALTURA = 600, 600
LINHAS, COLUNAS = 3, 3
TAMANHO_QUADRADO = LARGURA // COLUNAS

# Cores (RGB)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERMELHO = (242, 85, 96)
AZUL = (45, 137, 239)

# Configuração da Tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Velha - Pygame")
relogio = pygame.time.Clock()

# Matriz do Tabuleiro: 0 = Vazio, 1 = Jogador X, 2 = Jogador O
tabuleiro = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
turno_do_x = True
jogo_ativo = True

# --- Funções do Jogo ---

def desenhar_linhas():
    """Desenha a grade do tabuleiro."""
    tela.fill(BRANCO)
    # Linhas horizontais
    pygame.draw.line(tela, CINZA, (0, TAMANHO_QUADRADO), (LARGURA, TAMANHO_QUADRADO), 10)
    pygame.draw.line(tela, CINZA, (0, TAMANHO_QUADRADO * 2), (LARGURA, TAMANHO_QUADRADO * 2), 10)
    # Linhas verticais
    pygame.draw.line(tela, CINZA, (TAMANHO_QUADRADO, 0), (TAMANHO_QUADRADO, ALTURA), 10)
    pygame.draw.line(tela, CINZA, (TAMANHO_QUADRADO * 2, 0), (TAMANHO_QUADRADO * 2, ALTURA), 10)

def desenhar_figuras():
    """Desenha os X e O baseados na matriz do tabuleiro."""
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            # Calcular o centro do quadrado atual
            centro_x = coluna * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2
            centro_y = linha * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2

            if tabuleiro[linha][coluna] == 1:  # Desenha o X
                offset = 50
                pygame.draw.line(tela, VERMELHO, (centro_x - offset, centro_y - offset), (centro_x + offset, centro_y + offset), 15)
                pygame.draw.line(tela, VERMELHO, (centro_x - offset, centro_y + offset), (centro_x + offset, centro_y - offset), 15)
            
            elif tabuleiro[linha][coluna] == 2:  # Desenha o O
                pygame.draw.circle(tela, AZUL, (centro_x, centro_y), 50, 15)

def verificar_vitoria(jogador):
    """Checa se o jogador atual venceu."""
    # Verificar linhas
    for linha in range(LINHAS):
        if tabuleiro[linha][0] == jogador and tabuleiro[linha][1] == jogador and tabuleiro[linha][2] == jogador:
            return True
    # Verificar colunas
    for coluna in range(COLUNAS):
        if tabuleiro[0][coluna] == jogador and tabuleiro[1][coluna] == jogador and tabuleiro[2][coluna] == jogador:
            return True
    # Verificar diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    
    return False

def tabuleiro_cheio():
    """Verifica se deu empate (velha)."""
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if tabuleiro[linha][coluna] == 0:
                return False
    return True

def reiniciar_jogo():
    """Limpa a matriz para começar uma nova partida."""
    global tabuleiro, turno_do_x, jogo_ativo
    tabuleiro = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
    turno_do_x = True
    jogo_ativo = True
    desenhar_linhas()

# Inicializa o desenho inicial
desenhar_linhas()

# --- GAME LOOP ---
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Clique do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN and jogo_ativo:
            mouse_x = evento.pos[0]
            mouse_y = evento.pos[1]

            # Converte a posição do clique (pixels) para índices da matriz (0, 1 ou 2)
            coluna_clicada = mouse_x // TAMANHO_QUADRADO
            linha_clicada = mouse_y // TAMANHO_QUADRADO

            # Verifica se o quadrado está vazio
            if tabuleiro[linha_clicada][coluna_clicada] == 0:
                if turno_do_x:
                    tabuleiro[linha_clicada][coluna_clicada] = 1
                    if verificar_vitoria(1):
                        pygame.display.set_caption("Jogador X (Vermelho) Venceu!")
                        jogo_ativo = False
                    turno_do_x = False
                else:
                    tabuleiro[linha_clicada][coluna_clicada] = 2
                    if verificar_vitoria(2):
                        pygame.display.set_caption("Jogador O (Azul) Venceu!")
                        jogo_ativo = False
                    turno_do_x = True

                if tabuleiro_cheio() and jogo_ativo:
                    pygame.display.set_caption("Deu Velha! Empate.")
                    jogo_ativo = False

                desenhar_figuras()

        # Pressionar a tecla 'R' reinicia o jogo
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                reiniciar_jogo()
                pygame.display.set_caption("Jogo da Velha - Pygame")

    pygame.display.flip()
    relogio.tick(60)
