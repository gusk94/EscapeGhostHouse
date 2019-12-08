import pygame
from datetime import timedelta, datetime
import random

RED = (255, 0, 0)        # 적색:   적 255, 녹   0, 청   0
GREEN = (0, 255, 0)      # 녹색:   적   0, 녹 255, 청   0
BLUE = (0, 0, 255)       # 청색:   적   0, 녹   0, 청 255
PURPLE = (127, 0, 127)   # 보라색: 적 127, 녹   0, 청 127
BLACK = (0, 0, 0)        # 검은색: 적   0, 녹   0, 청   0
GRAY = (127, 127, 127)   # 회색:   적 127, 녹 127, 청 127
WHITE = (255, 255, 255)  # 하얀색: 적 255, 녹 255, 청 255

def drawBackground(screen):
    background = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, WHITE, background)


def drawRect(screen, color, position):
    block = pygame.Rect((position[1] * BlOCK_SIZE, position[0] * BlOCK_SIZE), (BlOCK_SIZE, BlOCK_SIZE))
    pygame.draw.rect(screen, color, block)


class Snake:
    color = GREEN

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]
        self.direction = 'up'
    
    def draw(self, screen):
        for position in self.positions:
            drawRect(screen, self.color, position)
    
    def crawl(self):
        
        head_position = self.positions[0]
        y, x = head_position
        dx, dy = DELTA_ON_DIRECTION[self.direction]
        self.positions = [(y + dy, x + dx)] + self.positions[:-1]
        # if self.direction == 'up':
        #     self.positions = [(y - 1, x)] + self.positions[:-1]
        # elif self.direction == 'down':
        #     self.positions = [(y + 1, x)] + self.positions[:-1]
        # elif self.direction == 'left':
        #     self.positions = [(y, x - 1)] + self.positions[:-1]
        # elif self.direction == 'right':
        #     self.positions = [(y, x + 1)] + self.positions[:-1]

    def turn(self, direction):
        self.direction = direction
    
    def grow(self):
        tail_position = self.positions[-1]
        y, x = tail_position

        self.positions.append((y, x))

class Apple:
    color = RED

    def __init__(self, position=(5, 5)):
        self.position = position
    
    def draw(self, screen):
        drawRect(screen, self.color, self.position)



class GameBoard:
    width = 20
    height = 20

    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()
    
    def draw(self, screen):
        self.apple.draw(screen)
        self.snake.draw(screen)

    def process_turn(self):
        self.snake.crawl()

        if self.snake.positions[0] == self.apple.position:
            self.snake.grow()
            self.put_new_apple()

    def put_new_apple(self):
        self.apple = Apple((random.randint(0, 19), random.randint(0, 19)))
        for position in self.snake.positions:
            if position == self.apple.position:
                self.put_new_apple()
                break

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BlOCK_SIZE = 20
TURN_INTERVAL = timedelta(seconds=0.3)
pygame.init()

DIRECTION_ON_KEY = {
    pygame.K_UP: 'up',
    pygame.K_DOWN: 'down',
    pygame.K_RIGHT: 'right',
    pygame.K_LEFT: 'left'
}

DELTA_ON_DIRECTION = {
    'up': (0, -1),
    'down': (0, 1),
    'right': (1, 0),
    'left': (-1, 0)
}

DIRECTION_ASIDE = {
    'up' : 'down',
    'down' : 'up',
    'right' : 'left',
    'left' : 'right'
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

drawRect(screen, WHITE, (1, 1))
drawRect(screen, GREEN, (2, 2))
block_position = [0, 0]
last_move_time = datetime.now()
now_direction = 'right'

game_board = GameBoard()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN and event.key in [pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT]:
            if DIRECTION_ON_KEY[event.key] == DIRECTION_ASIDE[game_board.snake.direction]:
                continue
            game_board.snake.turn(DIRECTION_ON_KEY[event.key])
            # dx, dy = DELTA_ON_DIRECTION[DIRECTION_ON_KEY[event.key]]
            # block_position[0] += dy
            # block_position[1] += dx
            # now_direction = DIRECTION_ON_KEY[event.key]
        
    # if timedelta(seconds=1) <= datetime.now() - last_move_time:
    #     dx, dy = DELTA_ON_DIRECTION[now_direction]
    #     block_position[0] += dy
    #     block_position[1] += dx            
    #     last_move_time = datetime.now()
    
    if TURN_INTERVAL < datetime.now() - last_move_time:
        game_board.process_turn()
        last_move_time = datetime.now()

    drawBackground(screen)
    # drawRect(screen, RED, block_position)
    game_board.draw(screen)
    
    pygame.display.update()
