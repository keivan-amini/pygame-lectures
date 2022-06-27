import random
import sys
import pygame
import player

# per far partire i processi di pygame, devo far partire l' init
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Montecreto Mount of Madness")
screen = pygame.display.set_mode((800, 600))

# image zone
image = pygame.image.load("C:\\Users\\ASUS\\OneDrive - Alma Mater Studiorum Università di Bologna\\Documents\\Lavoro - Educatore Digitale\\Montecreto\\giochi dei ragazzi\\Alex\\img\\Luigi.png")
mario1 = player.Player(image, (400, 300))

# sprite zone
player_group = pygame.sprite.Group()
player_group.add(mario1)


# gameplay cycle
while True:
    # INPUT CONTROL AREA
    for event in pygame.event.get():
        # key press event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mario1.rect.x += 10

        # se l'evento è di tipo QUIT...
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update area
    player_group.update()

    # draw area
    screen.fill("#45d1a0")
    player_group.draw(screen)
    pygame.display.update()
    clock.tick(60)