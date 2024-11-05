import pygame
from pygame.locals import *
import os

class bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super(bullet, self).__init__()
        
        # Carrega a imagem do missil
        bullet_image_path = os.path.join(os.path.dirname(__file__), 'bullet.png')
        self.surf = pygame.image.load(bullet_image_path).convert_alpha()  # Usa a imagem
        self.surf = pygame.transform.rotate(self.surf, 90)  # Rotaciona a imagem
        self.surf = pygame.transform.scale(self.surf, (40, 40))

        # Inicializa a posição do missil de acordo com a posiçao do player
        self.rect = self.surf.get_rect(center=(player.rect.centerx, player.rect.centery))
        self.hitbox =pygame.Rect(self.rect.x + 10, self.rect.y + 10, 20, 20)
        self.speed = 15

    def update(self): 
        self.rect.move_ip(self.speed, 0)  # Move o missil para a direita
        self.hitbox.topleft = self.rect.topleft
        if self.rect.right > 800:  # Verifica se o missil saiu da tela
            self.kill()  # Remove o missil

""""
for bullet in bullets:
        enemy_hit = pygame.sprite.spritecollideany(bullet, enemies)
        if enemy_hit:
            bullet.kill()
            enemy_hit.kill()
"""
