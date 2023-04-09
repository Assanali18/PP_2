import pygame, sys, time
from pygame.locals import *
from random import randrange, choice
from threading import Timer

pygame.init()

clock = pygame.time.Clock()
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255,140,0)

# Variables
screen_w = 900
screen_h = 700
SPEED = 50
dx, dy = 0,0
k = False



# Fonts
font = pygame.font.SysFont("Arial", 60, bold=True)
font_small = pygame.font.SysFont("Arial", 26)
end = font.render("GAME OVER", True, ORANGE)

# Background atributes 
background = pygame.image.load(r"atributes\snake_folder\new.bg.jpg")
background = pygame.transform.scale(background, (screen_w,screen_h))
# pygame.mixer.music.load(r'atributes\bg_snake_sound.mp3')
# pygame.mixer.music.play()

# Creating of screen
SCREEN = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Snake')




class Fruit:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load(r'atributes\snake_folder\apple.png'), (40, 40))
        self.rect = self.image.get_rect()
        self.pos = (randrange(50,screen_w, SPEED), randrange(50,screen_h, SPEED))
        self.rect.topleft = (self.pos)
        self.W = choiceWidth()
    def draw_fruit(self):
        SCREEN.blit(self.image, self.rect)
    def new_fruit(self):
        self.image = pygame.transform.scale(pygame.image.load(r'atributes\snake_folder\apple.png'), (self.W, self.W))
        self.rect = self.image.get_rect()
        self.pos = (randrange(50,screen_w, SPEED), randrange(50,screen_h, SPEED))
        self.rect.topleft = (self.pos)
        SCREEN.blit(self.image, self.rect)
        self.timer = Timer(2, fruit.new_fruit)
        
        

class Snake:
    def __init__(self):
        self.x = screen_w/2
        self.y = screen_h/2
        self.body = []
        self.body.append((self.x, self.y))
        self.lenght = 1
        self.score = 0
        self.FPS = 150

    def draw_snake(self):
        self.rect = [pygame.draw.rect(SCREEN, GREEN, (i,j, SPEED-2, SPEED-2)) for i,j in self.body]
        
    def move_snake(self, dx, dy):
        self.dx, self.dy = dx, dy
        self.x += self.dx * SPEED
        self.y += self.dy * SPEED
        self.body.append((self.x, self.y))
        self.body = self.body[-self.lenght:]
        
# Chech collision
def check_collision():
    global timer,k
    if snake.body[-1] == fruit.pos:
        if k:
            fruit.timer.cancel()
            k = False
        if fruit.W == 40: snake.score += 1
        else: snake.score += 2
        fruit.W = choiceWidth()
        fruit.new_fruit()
        if fruit.W == 50: 
            fruit.W = choiceWidth()
            fruit.timer.start()
            k = True

        snake.lenght += 1
        pygame.mixer.music.load(r'atributes\snake_folder\apple_sound.mp3')
        pygame.mixer.music.play()


    if snake.score % 2 == 0 and snake.FPS != 70:
        snake.FPS -= 5
    
# Drawing the score display
def draw_score():
    scores = font_small.render(f'{snake.score}', True, (65, 74,12))
    score_rect = scores.get_rect(center = (60, 40))
    apple_rect = pygame.transform.scale(pygame.image.load(r'atributes\snake_folder\apple.png'), (25, 25)).get_rect(midright = (score_rect.left, score_rect.centery))
    pygame.draw.rect(SCREEN, ORANGE,(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width, apple_rect.height ))
    SCREEN.blit(scores, score_rect)
    SCREEN.blit(pygame.transform.scale(pygame.image.load(r'atributes\snake_folder\apple.png'), (20, 20)), apple_rect)
    pygame.draw.rect(SCREEN, WHITE,(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width, apple_rect.height ), 1)
# Game over
def check_fail():
    if snake.x >= screen_w or snake.x < 0 or snake.y >= screen_h or snake.y < 0:
        game_over()
    # if snake.lenght >=2:
    for block in snake.body[:-1]:
        if snake.x == block[0] and snake.y == block[1]:
            game_over()

def game_over():
    while True:
        SCREEN.blit(end, (screen_w//2-150,screen_h//3))
        SCREEN.blit(font_small.render(f"Your points:{snake.score}",True, ORANGE ), (screen_w//2-55, screen_h//3 + 80))
        pygame.display.update()
        for event in pygame.event.get(): 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
def choiceWidth():
    return choice([40, 40, 40, 40, 50, 40])



fruit = Fruit()
snake = Snake()


# Boost FPS
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, snake.FPS)



 





while True:        
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake(dx, dy)


    SCREEN.blit(background, (0,0))

    fruit.draw_fruit()
    snake.draw_snake()
    check_collision()
    check_fail()
    draw_score()
    
    # Control
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_w] or pressed_keys[K_UP]:
        dx, dy = 0, -1
    if pressed_keys[K_s] or pressed_keys[K_DOWN]:
        dx, dy = 0, 1
    if pressed_keys[K_a] or pressed_keys[K_LEFT]:
        dx, dy = -1, 0
    if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
        dx, dy = 1, 0


    pygame.display.update()
    clock.tick(240)

