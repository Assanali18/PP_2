import pygame
import datetime
import math

pygame.init()

# Создание экрана
screen_width = 1400
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))



# Загрузка изображений стрелок и часов
clock_image = pygame.image.load("atributes\images\mainclock.PNG")
hour_image = pygame.image.load("atributes\images\hourIMG.png")
minute_image = pygame.image.load("atributes\images\minIMG.png")

# Создание библеотеки с системой времени
clock60 = dict(zip(range(60), range(0,360, 6)))

# Установка часов 
pos = (screen_width/2,screen_height/2) 

# Основная функция
def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = ((pos[0] - originPos[0]), (pos[1]-originPos[1])))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y))

    surf.blit(rotated_image, rotated_image_rect)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Работа с экраном
    screen.fill(pygame.Color('black'))
    micky_rect = clock_image.get_rect(topleft = (270,-70)) 
    screen.blit(clock_image, micky_rect) 

    # Использование времени
    t = datetime.datetime.now() 
    hour, minute, second = ((t.hour%12)*5+t.minute//12), t.minute, t.second

    # Использование функций
    blitRotate(screen, hour_image, pos, (25, 210), -clock60[hour]) 
    blitRotate(screen, minute_image, pos, (25, 272), -clock60[minute])   

    # Устновка таймера
    font = pygame.font.SysFont('Verdana', 60) 
    time_render = font.render(f'{t:%H:%M:%S}',None, pygame.Color('orange'))
    screen.blit(time_render, (0, 0))

    pygame.display.flip()

pygame.quit()
