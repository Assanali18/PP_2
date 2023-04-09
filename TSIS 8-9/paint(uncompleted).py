import pygame, sys


pygame.init()
clock = pygame.time.Clock()
screen_width = 700
screen_height =500


# Colors
white = (255, 255, 255)
blue = (67,238,250)
red = (255, 0, 0)
black = (0, 0, 0)
green = (38,245,45)
pink = (255,192,203)
orange = (255,165,0)
yellow = (255,255,0)
violet = (177, 3, 252)

pencolour = black

# Create screen
screen =  pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Paint")
screen.fill((white))

# Backgound
backimg = pygame.image.load("atributes\paint_folder\paint.png").convert_alpha()
backimg = pygame.transform.scale(backimg, (screen_width, screen_height))
screen.blit(backimg, (0,0))

#rect for the drawing area
draw_area = 119, 17, 562, 465


# Value of rect (x,y, width, height)
col1= (22, 81, 30, 34)
col2= (56, 81, 34, 34)
col3= (22, 120, 30, 33)
col4= (56, 120, 34, 32)
col5= (22, 156, 30, 33)
col6= (56, 156, 34, 32)
col7= (22, 192, 30, 33)
col8= (56, 192, 34, 32)

#Rect that highlight which button is selected
buttonselect = (22, 81, 30, 34)

#Function to draw color box
def drawRectangleColor():    
    pygame.draw.rect(screen, black, col1)
    pygame.draw.rect(screen,blue, col2,)
    pygame.draw.rect(screen, red, col3)
    pygame.draw.rect(screen, green, col4)
    pygame.draw.rect(screen, pink, col5)
    pygame.draw.rect(screen, orange, col6)
    pygame.draw.rect(screen, yellow, col7)
    pygame.draw.rect(screen, violet, col8)
    # figure
    pygame.draw.rect(screen, black, (13, 320, 40, 20))
    pygame.draw.circle(screen, black, (80, 330), 12 )    
drawRectangleColor()

# Pencil
class Pencil:
    def __init__(self):
        self.prevX = 0
        self.prevY = 0
        self.isMouseDown = False
        
    def drawline(self, pencolour):
        self.running = True
        while self.running:
            self.pencolour = pencolour
            self.currentX = self.prevX
            self.currentY = self.prevY
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: 
                            self.isMouseDown = True

                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1: 
                            self.isMouseDown = False

                    if event.type == pygame.MOUSEMOTION and 122 < event.pos[0] < 678 and 21 < event.pos[1] < 480 :
                        # if mouse moved, add point to list
                        self.currentX =  event.pos[0]
                        self.currentY =  event.pos[1]
                        
            if self.isMouseDown:
                pygame.draw.line(screen, self.pencolour, (self.prevX, self.prevY), (self.currentX, self.currentY),3)
            self.prevX = self.currentX
            self.prevY = self.currentY
            pencil.exitDrawLine()
            pygame.display.flip()
            
    def exitDrawLine(self):
        self.t = pygame.mouse.get_pressed()
        if self.t[0] == 1:     
            self.mousepos = pygame.mouse.get_pos()
            if 0 < self.mousepos[0] < 122 and 21 < self.mousepos[1] < 480:
                self.running = False


class Rectangle:
    def __init__(self):
        self.prevX = -1
        self.prevY = -1
        self.currentX = -1
        self.currentY = -1
        self.draw_layer = pygame.Surface((562, 465))
        self.draw_layer.fill((50, 100, 50))
        self.baseLayer = pygame.Surface((562, 465))
        self.isMouseDown = False
    def drawrectangle(self):
        print(1)
        self.running = True
        while self.running:
            self.pencolour = pencolour
            rectangle.exitDrawRect()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        self.isMouseDown = True
                        self.currentX =  event.pos[0]
                        self.currentY =  event.pos[1]    
                        self.prevX =  event.pos[0]
                        self.prevY =  event.pos[1]

                if event.type == pygame.MOUSEBUTTONUP:
                    self.isMouseDown = False
                    self.baseLayer.blit(self.draw_layer, (119, 17))


                if event.type == pygame.MOUSEMOTION:
                    if self.isMouseDown:
                        self.currentX =  event.pos[0]
                        self.currentY =  event.pos[1]
            

            if self.isMouseDown and self.prevX != -1 and self.prevY != -1 and self.currentX != -1 and self.currentY != -1 and  122 < self.currentX < 678 and 21 < self.currentY < 480:
                self.draw_layer.blit(self.baseLayer, (119, 17))
                self.r = pygame.Rect(min(self.prevX, self.currentX), min(self.prevY, self.currentY), abs(self.prevX - self.currentX), abs(self.prevY - self.currentY))
                pygame.draw.rect(screen, (0,0,0),self.r, 1)

        
            pygame.display.flip()
        
    

    def exitDrawRect(self):
        self.t = pygame.mouse.get_pressed()
        if self.t[0] == 1:     
            self.mousepos = pygame.mouse.get_pos()
            if 0 < self.mousepos[0] < 122 and 21 < self.mousepos[1] < 480:

                self.running = False



def drawcircle():
    pass




#Set mouse cursor for pencil 
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
is_rect = False
is_circle = False
is_line = False

pencil = Pencil()
rectangle = Rectangle()



#Gameloop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      
      # Create border
        pygame.draw.rect(screen, white, buttonselect, 2)



        t = pygame.mouse.get_pressed()
        if t[0] == 1:     
            mousepos = pygame.mouse.get_pos()

        

            # Drawing on screen
            if 122 < mousepos[0] < 678 and 21 < mousepos[1] < 480:
                
                # if is_rect:
                    rectangle.drawrectangle()
                #     pygame.draw.rect(screen, pencolour, (mousepos[0], mousepos[1], 100, 70), 2)
                # elif is_circle:
                #     pygame.draw.circle(screen, pencolour, (mousepos[0], mousepos[1]), 40, 2 )

                # else:
                #     pencil.drawline(pencolour)

                

            
            # Rectangle
            elif 13 < mousepos[0] < 53 and 320< mousepos[1] < 340:
                is_rect = True
                # rectangle.drawrectangle(pencolour)
                is_circle = False
                is_line = False
                drawRectangleColor()  
                pygame.draw.rect(screen, black, (13, 320, 40, 20))
                pygame.draw.rect(screen, white, (13, 320, 40, 20), 2)
                # rectangle.drawrectangle(pencolour)

                
            # Circle
            elif 68 < mousepos[0] < 92 and 318< mousepos[1] < 342:
                is_circle = True
                is_rect = False
                is_line = False
                drawRectangleColor() 
                pygame.draw.circle(screen, black, (80, 330), 12)    
                pygame.draw.circle(screen, white, (80, 330), 12, 2 )
                    
            # Colors    
            elif 22 < mousepos[0] < 52 and 81 < mousepos[1] < 115:
                pencolour = black
                drawRectangleColor()         
                buttonselect = (22, 81, 30, 34)
                is_rect = False
                is_circle = False
                is_line = False
                
            elif 56 < mousepos[0] < 90 and 81 < mousepos[1] < 115:
                pencolour = blue
                drawRectangleColor()
                buttonselect = (56, 81, 34, 34)
                is_rect = False
                is_circle = False
                is_line = False
                
            elif 22 < mousepos[0] < 52 and 120 < mousepos[1] < 153:
                pencolour = red
                drawRectangleColor()
                buttonselect = (22, 120, 30, 33)
                is_rect = False
                is_circle = False
                is_line = False
                
            elif 56 < mousepos[0] < 90 and 120 < mousepos[1] < 152:
                pencolour = green
                drawRectangleColor()
                buttonselect = (56, 120, 34, 32)
                is_rect = False
                is_circle = False
                is_line = False
                
            elif 22 < mousepos[0] < 52 and 156 < mousepos[1] < 189:
                pencolour = pink
                drawRectangleColor()
                buttonselect = (22, 156, 30, 33)
                is_rect = False
                is_circle = False
                is_line = False
                
            elif 56 < mousepos[0] < 90 and 156 < mousepos[1] < 188:
                pencolour = orange
                drawRectangleColor()
                buttonselect = (56, 156, 34, 32)
                is_rect = False
                is_circle = False
                is_line = False
                
            elif 22 < mousepos[0] < 52 and 192 < mousepos[1] < 225:
                pencolour = yellow
                drawRectangleColor()
                buttonselect = (22, 192, 30, 33)
                is_rect = False
                is_circle = False
                is_line = False
                
            elif 56 < mousepos[0] < 90 and 192 < mousepos[1] < 224:
                pencolour = violet
                drawRectangleColor()
                buttonselect = (56, 192, 34, 32)
                is_rect = False
                is_circle = False
                is_line = False

            #Eraser
            elif 13 < mousepos[0] < 54 and 247 < mousepos[1] < 285:
                pencolour = white
                drawRectangleColor()
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
                is_rect = False
                is_circle = False
                is_line = False
            #Pencil
            elif 59 < mousepos[0] < 97 and 247 < mousepos[1] < 288:
                pencolour = black
                drawRectangleColor()
                is_line = True
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                # pencil.drawline(pencolour)
                buttonselect = (22, 81, 30, 34)
                is_rect = False
                is_circle = False
                
            elif 15 < mousepos[0] < 96 and 363 < mousepos[1] < 400:                
                pygame.draw.rect(screen, white, draw_area)
                is_rect = False
                is_circle = False
                is_line = False

        
        pygame.display.update()
        clock.tick(120)
                
            
