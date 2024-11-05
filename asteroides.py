import pygame
import random
import os

# Classe que representa os inimigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        
        # Carrega a imagem do asteroide
        asteroid_image_path = os.path.join(os.path.dirname(__file__), 'asteroid.png')
        self.surf = pygame.image.load(asteroid_image_path).convert_alpha()  # Usa a imagem do asteroide
        
        # Redimensiona a imagem
        self.surf = pygame.transform.scale(self.surf, (140, 140))

        # Inicializa a posição do inimigo na extrema direita e sorteia sua posição em relação à coordenada y
        self.rect = self.surf.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.speed = random.uniform(5, 10)  # Sorteia sua velocidade, entre 1 e 15

    # Função que atualiza a posição do inimigo em função da sua velocidade e remove-o quando atinge o limite esquerdo da tela
    def update(self):
        self.rect.move_ip(-self.speed, 0)  # Move o inimigo para a esquerda
        if self.rect.right < 0:  # Verifica se o inimigo saiu da tela
            self.kill()  # Remove o inimigo
