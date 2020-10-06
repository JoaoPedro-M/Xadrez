import pygame
import sys


class Peca(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('pecas/bispo.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 30, 30








pygame.init()
tela = pygame.display.set_mode([1000, 800])
pygame.display.set_caption('Xadrez')

tempo = pygame.time.Clock()

cav = Peca()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            cav.rect.x = x
            cav.rect.y = y
    tela.fill((0, 0, 0))

    tela.blit(cav.image, [cav.rect.x, cav.rect.y])

    tempo.tick(30)
    pygame.display.update()
