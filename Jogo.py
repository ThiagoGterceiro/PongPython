import pygame
import sys

pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong")

raquete_largura = 15
raquete_altura = 100
raquete_velocidade = 5
bola_raio = 10
bola_velocidade_x = 5
bola_velocidade_y = 5

x_raquete_esquerda = 30
y_raquete_esquerda = ALTURA // 2 - raquete_altura // 2
x_raquete_direita = LARGURA - 30 - raquete_largura
y_raquete_direita = ALTURA // 2 - raquete_altura // 2
bola_x = LARGURA // 2
bola_y = ALTURA // 2

placar_esquerda = 0
placar_direita = 0

relogio = pygame.time.Clock()

def salvar_placar():
    with open("placar.txt", "w") as arquivo:
        arquivo.write(f"Jogador Esquerdo: {placar_esquerda}\n")
        arquivo.write(f"Jogador Direito: {placar_direita}\n")

def desenha_jogo():
    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, (x_raquete_esquerda, y_raquete_esquerda, raquete_largura, raquete_altura))
    pygame.draw.rect(tela, BRANCO, (x_raquete_direita, y_raquete_direita, raquete_largura, raquete_altura))
    pygame.draw.circle(tela, BRANCO, (bola_x, bola_y), bola_raio)
    pygame.draw.aaline(tela, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA))

    fonte = pygame.font.Font(None, 36)
    texto_esquerda = fonte.render(str(placar_esquerda), True, BRANCO)
    texto_direita = fonte.render(str(placar_direita), True, BRANCO)
    
    tela.blit(texto_esquerda, (LARGURA // 4, 20))
    tela.blit(texto_direita, (LARGURA * 3 // 4, 20))

    pygame.display.update()

def move_bola():
    global bola_x, bola_y, bola_velocidade_x, bola_velocidade_y, placar_esquerda, placar_direita

    bola_x += bola_velocidade_x
    bola_y += bola_velocidade_y

    if bola_y - bola_raio <= 0 or bola_y + bola_raio >= ALTURA:
        bola_velocidade_y *= -1

    if (bola_x - bola_raio <= x_raquete_esquerda + raquete_largura and y_raquete_esquerda < bola_y < y_raquete_esquerda + raquete_altura) or \
       (bola_x + bola_raio >= x_raquete_direita and y_raquete_direita < bola_y < y_raquete_direita + raquete_altura):
        bola_velocidade_x *= -1

    if bola_x - bola_raio <= 0:
        placar_direita += 1
        salvar_placar()
        bola_x = LARGURA // 2
        bola_y = ALTURA // 2
        return True

    if bola_x + bola_raio >= LARGURA:
        placar_esquerda += 1
        salvar_placar()
        bola_x = LARGURA // 2
        bola_y = ALTURA // 2
        return True

    return False

def move_raquetes():
    global y_raquete_esquerda, y_raquete_direita

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w] and y_raquete_esquerda > 0:
        y_raquete_esquerda -= raquete_velocidade
    if teclas[pygame.K_s] and y_raquete_esquerda < ALTURA - raquete_altura:
        y_raquete_esquerda += raquete_velocidade

    if teclas[pygame.K_UP] and y_raquete_direita > 0:
        y_raquete_direita -= raquete_velocidade
    if teclas[pygame.K_DOWN] and y_raquete_direita < ALTURA - raquete_altura:
        y_raquete_direita += raquete_velocidade

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move_raquetes()
    if move_bola():
        print(f"Placar - Esquerda: {placar_esquerda} | Direita: {placar_direita}")

    desenha_jogo()
    relogio.tick(60)
