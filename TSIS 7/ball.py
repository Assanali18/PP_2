import pygame

pygame.init()

# Set screen dimensions and create a display surface
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Set ball properties
ball_radius = 25
ball_color = (255, 0, 0)
ball_x = screen_width // 2
ball_y = screen_height // 2

# Set movement properties
movement_step = 20
movement_x = 0
movement_y = 0


game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                movement_y = -movement_step
            elif event.key == pygame.K_DOWN:
                movement_y = movement_step
            elif event.key == pygame.K_LEFT:
                movement_x = -movement_step
            elif event.key == pygame.K_RIGHT:
                movement_x = movement_step
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                movement_y = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movement_x = 0
                
    # Update ball position
    ball_x += movement_x
    ball_y += movement_y
    
    # Check if ball is out of screen boundaries
    if ball_x - ball_radius < 0:
        ball_x = ball_radius
    elif ball_x + ball_radius > screen_width:
        ball_x = screen_width - ball_radius
        
    if ball_y - ball_radius < 0:
        ball_y = ball_radius
    elif ball_y + ball_radius > screen_height:
        ball_y = screen_height - ball_radius
    

    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    
    pygame.display.flip()
    clock.tick(10)

    
pygame.quit()
