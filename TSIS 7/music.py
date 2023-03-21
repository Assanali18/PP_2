import pygame
import os
import random
from time import sleep


pygame.init()

window = pygame.display.set_mode((500, 500))
window.fill(pygame.Color('aliceblue'))
pygame.display.set_caption("Pygame Music Player")

# Пути
music_folder = r"C:\PP2_tasks\TSIS 7\atributes\task2\music"
cover_folder = r'C:\PP2_tasks\TSIS 7\atributes\task2\cover_images'
music_files = os.listdir(music_folder)
cover_files = os.listdir(cover_folder)

pygame.mixer.init()
current_track = random.randint(0, len(music_files)-1)
# Load the image
cover = pygame.image.load(os.path.join(cover_folder, cover_files[current_track]))
rect_of_cover = cover.get_rect(center = (250, 150))
window.blit(cover, rect_of_cover)

# Load the music
pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
pygame.mixer.music.play()

# Load the icons
forw = pygame.image.load(r'atributes\task2\icons\forw.png')
forw_rect = forw.get_rect(topleft =  (125,325))
window.blit(forw, forw_rect)
stop = pygame.image.load(r'atributes\task2\icons\pause.png')
stop_rect = stop.get_rect(topleft =  (200,325))
window.blit(stop, stop_rect)
play = pygame.image.load(r'atributes\task2\icons\play.png')
play_rect = play.get_rect(topleft =  (275,325))
window.blit(play, play_rect)
back = pygame.image.load(r'atributes\task2\icons\back.png')
back_rect = back.get_rect(topleft =  (350,325))
window.blit(back, back_rect)

# Boolean  function
def boolClick(rect, mouse):
    if mouse[0] in range(rect.topleft[0], rect.topright[0])  and mouse[1]  in range(rect.topleft[1], rect.bottomleft[1]): return True

# Click event function
def ClickEvent(current_track):
    cover = pygame.image.load(os.path.join(cover_folder, cover_files[current_track]))
    window.blit(cover, rect_of_cover) 
    pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
    pygame.mixer.music.play()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            # Play the next track
            if event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                ClickEvent(current_track)
                
            # Play the previous track
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                ClickEvent(current_track)
            
            # Pause the music
            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            
            # Resume playing the music
            elif event.key == pygame.K_RETURN:
                pygame.mixer.music.unpause()

        elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if boolClick(forw_rect, mouse): 
                    current_track = (current_track - 1) % len(music_files)
                    ClickEvent(current_track)

                elif boolClick(back_rect, mouse):
                    current_track = (current_track + 1) % len(music_files)
                    ClickEvent(current_track)

                elif boolClick(stop_rect, mouse):
                    pygame.mixer.music.pause()  

                elif boolClick(play_rect, mouse):
                    pygame.mixer.music.unpause()

    pygame.display.update()
