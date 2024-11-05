# Biblioteca PyGame
import pygame
from pygame.locals import *
from bullets import bullet
from asteroides import Enemy
from jogador import Player
import os

# Inicializa pygame
pygame.init()

screen_width = 800  # Largura da tela ou eixo x
screen_height = 600  # Altura da tela ou eixo y
screen = pygame.display.set_mode((screen_width, screen_height))  # Cria a tela com o tamanho definido
pygame.display.set_caption("SpaceX Alpha")  # Define o nome da janela "SpaceX Alpha"
background = pygame.image.load(os.path.join(os.path.dirname(__file__), 'packground.png')).convert()  # define a imagem de plano de fundo
screen.blit(background, (0, 0))  # coloca a imagem de plano de fundo na tela e define sua posição

pygame.display.flip()
clock = pygame.time.Clock()

# Define os eventos para criação de inimigos e mísseis
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)  # Intervalo de criação de inimigos

# Cria o jogador
player = Player()

# Define o plano de fundo (cor branca)
# background = pygame.Surface(screen.get_size())
# background.fill((0, 0, 0))

# Placar
score = 0

# Formatação para placar
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Grupos de sprites
missil = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Variável de estado do jogo
game_over = False

def check_collisions():
    global game_over, score
    if pygame.sprite.spritecollideany(player, enemies):
        game_over = True

    # Verifica colisões entre mísseis e inimigos
    for tiros in missil:
        enemy_hit = pygame.sprite.spritecollideany(tiros, enemies)
        if enemy_hit:
            tiros.kill()
            enemy_hit.kill()
            score += 10  # Incrementa o placar quando um inimigo é destruído

def show_game_over_screen():
    game_over_font = pygame.font.SysFont(None, 72)
    game_over_surf = game_over_font.render('Game Over', True, (255, 0, 0))
    game_over_rect = game_over_surf.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    screen.blit(game_over_surf, game_over_rect)

    score_font = pygame.font.SysFont(None, 48)
    score_surf = score_font.render(f'Score: {score}', True, (255, 255, 255))
    score_rect = score_surf.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    screen.blit(score_surf, score_rect)

def draw_score():
    score_surf = font.render(f'Score: {score}', True, (255, 255, 255))
    score_rect = score_surf.get_rect(topright=(screen_width - 10, 10))
    screen.blit(score_surf, score_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
        elif event.type == KEYDOWN and event.key == K_SPACE and not game_over:
            new_bullet = bullet(player)
            missil.add(new_bullet)

    pressed_keys = pygame.key.get_pressed()

    if not game_over:
        player.update(pressed_keys, missil)
        enemies.update()
        missil.update()

    check_collisions()

    screen.blit(background, (0, 0))
    for entity in [player] + list(enemies) + list(missil):
        screen.blit(entity.surf, entity.rect)

    if game_over:
        show_game_over_screen()
    else:
        draw_score()

    pygame.display.flip()
    clock.tick(60)