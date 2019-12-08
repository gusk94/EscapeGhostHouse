import pygame
from datetime import datetime, timedelta
from resource import player, maps, monsters, traps, gameboard, colors
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BLOCK_SIZE = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()
screen.fill(colors.WHITE)
ghost = pygame.image.load('static/image/player/ghost1.png')
ghost = pygame.transform.scale(ghost, (50, 50))

rect = pygame.Rect((0, 0), (50, 50))

pygame.draw.rect(screen, colors.RED, rect)

screen.blit(ghost, (400, 400))
pygame.display.update()


time.sleep(3)