import pygame
import math

pygame.init()

WIDTH = 740
HEIGHT = 580
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

ghost_x = WIDTH
ghost_y = 300
ghost_x_speed = 5
ghost_y_speed = 1
ghost_radius = 40

ghost_x2 = 400
ghost_y2 = 200
angle = math.pi
direction = 1

candy_x = 200
candy_y = 0
candy_y_speed = 3.6

candy_x2 = 390
candy_y2 = 0
candy_y2_speed = 3.6

candy_x3 = 518
candy_y3 = 0
candy_y3_speed = 4

square_y = 270
square_y_speed = 1.2

square_y2 = 270
square_y2_speed = 1.2
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
       
        #1

    ghost_x2 =  WIDTH // 2 + math.cos(angle) * 370
    ghost_y2 = (HEIGHT + 100) + math.sin(angle) * 370

    if angle >= 2 * math.pi: 
        angle = 2 * math.pi
        direction = -1
    elif angle <= math.pi:
        angle = math.pi
        direction = 1

    angle += 0.03 * direction


    #2
    ghost_x += -ghost_x_speed 
    ghost_y += -ghost_y_speed 
       
    if ghost_x <= -2 * ghost_radius:
        ghost_x_speed *= -1
        host_y2_speed = 2 
   
    if ghost_x >= WIDTH + ghost_radius:   
           ghost_x_speed *= -1
           ghost_y_speed *= 2
       
    if ghost_y <= -2 * ghost_radius:
           ghost_y_speed *= -1
                 
    if ghost_y >= HEIGHT + ghost_radius:
           ghost_y_speed = 5
    
     #candy  
    candy_y += candy_y_speed
    if candy_y >= 440:
          candy_y_speed = 0

    candy_y2 += candy_y2_speed
    if candy_y2 >= 407:
        candy_y2_speed = 0   

    candy_y3 += candy_y3_speed
    if candy_y3 >= 442:
        candy_y3_speed = 0

    #square
    square_y2 += square_y_speed
    if square_y2 >= 285:
        square_y2_speed *= -1
    elif square_y2 <= 245:
        square_y2_speed *= -1

    square_y += square_y_speed
    if square_y >= 285:
        square_y_speed *= -1
    elif square_y <= 245:
        square_y_speed *= -1

    

    # DRAWING
    screen.fill((255,117,24))

    #pumpkin face
    pumpkin_eyes_color = (255,184,0)
    pygame.draw.circle(screen,pumpkin_eyes_color,(260,250), 25)
    pygame.draw.circle(screen,pumpkin_eyes_color,(465,250), 25)
    rect = (235,250,50,40)
    pygame.draw.rect(screen,pumpkin_eyes_color,rect)
    rect = (440,250,50,40)
    pygame.draw.rect(screen,pumpkin_eyes_color,rect)

    rect = (235,square_y,50,80)
    pygame.draw.rect(screen,(255,117,24),rect)
    
    rect = (440,square_y2,50,80)
    pygame.draw.rect(screen,(255,117,24),rect)

     #gravestones
    #1
    grey_color = (57,60,61)
    rect =(170,450,120,130)
    pygame.draw.rect(screen, grey_color,rect)
    #2
    rect =(328,417,120,130)
    pygame.draw.rect(screen, grey_color,rect)
    #3
    rect =(480,455,120,130)
    pygame.draw.rect(screen, grey_color,rect)
    
    white_color2 = (235,236,240)
    
    rect =(195,460,70,20)
    pygame.draw.rect(screen, white_color2,rect)
    #2
    rect =(353,427,70,20)
    pygame.draw.rect(screen, white_color2,rect)
    #3
    rect =(505,465,70,20)
    pygame.draw.rect(screen, white_color2,rect)
         
    #hill
    rect =(-50, HEIGHT - 50, WIDTH + 100, HEIGHT // 2)
    pygame.draw.ellipse(screen, (140,146,172), rect)

    #candy rain
    red_color = (152,38,8)
    pygame.draw.circle(screen,red_color,(candy_x,candy_y), 10)
    pygame.draw.polygon(screen,red_color,((candy_x-15,candy_y-8),(candy_x-15,candy_y+8),(candy_x-5,candy_y)))
    pygame.draw.polygon(screen,red_color,((candy_x+15,candy_y-8),(candy_x+15,candy_y+8),(candy_x+5,candy_y))) 
       
    blue_color = (72,74,170)
    pygame.draw.circle(screen,blue_color,(candy_x2,candy_y2), 10)
    pygame.draw.polygon(screen,blue_color,((candy_x2-15,candy_y2-8),(candy_x2-15,candy_y2+8),(candy_x2-5,candy_y2)))
    pygame.draw.polygon(screen,blue_color,((candy_x2+15,candy_y2-8),(candy_x2+15,candy_y2+8),(candy_x2+5,candy_y2))) 
    
    green_color = (82,172,0)
    pygame.draw.circle(screen,green_color,(candy_x3,candy_y3), 8)
    pygame.draw.polygon(screen,green_color,((candy_x3-15,candy_y3-8),(candy_x3-15,candy_y3+8),(candy_x3-5,candy_y3)))
    pygame.draw.polygon(screen,green_color,((candy_x3+15,candy_y3-8),(candy_x3+15,candy_y3+8),(candy_x3+5,candy_y3))) 
    
    
     #Ghosts
     #ghost1
    white_color = (242,232,220)
    eyes_color = (136, 91, 64)
    grey_color = (79,72,72)
    pygame.draw.circle(screen, white_color,(ghost_x, ghost_y), 40)
         
    rect =(ghost_x - ghost_radius,ghost_y,80,55)
    pygame.draw.rect(screen, white_color,rect)
    pygame.draw.circle(screen, white_color,(ghost_x - 27 , ghost_y + 61), 13)
    pygame.draw.circle(screen, white_color,(ghost_x - 5, ghost_y + 61), 13)
    pygame.draw.circle(screen, white_color,(ghost_x + 15, ghost_y + 61), 13)
    pygame.draw.circle(screen, white_color,(ghost_x + 30, ghost_y + 61), 13)
             
        
    pygame.draw.circle(screen,eyes_color,(ghost_x +15, ghost_y+15), 10)    
    pygame.draw.circle(screen,eyes_color,(ghost_x +16, ghost_y+18), 10)     
    pygame.draw.circle(screen,eyes_color,(ghost_x -15, ghost_y+15), 10)
    pygame.draw.circle(screen,eyes_color,(ghost_x -13, ghost_y+12), 10)
    pygame.draw.polygon(screen,grey_color,((ghost_x,ghost_y + 25),(ghost_x - 6,ghost_y + 33),(ghost_x + 6,ghost_y+ 33)))
    
      #goast2
    white_color = (242,232,220)
    eyes_color = (136, 91, 64)
    pygame.draw.circle(screen, white_color,(ghost_x2, ghost_y2), 40)
   
    rect =(ghost_x2 - ghost_radius,ghost_y2,80,55)
    pygame.draw.rect(screen, white_color,rect)
    pygame.draw.circle(screen, white_color,(ghost_x2 - 35, ghost_y2 + 61), 13)
    pygame.draw.circle(screen, white_color,(ghost_x2 - 15, ghost_y2 + 61), 13)
    pygame.draw.circle(screen, white_color,(ghost_x2 +5, ghost_y2 + 61), 13)
    pygame.draw.circle(screen, white_color,(ghost_x2 + 25, ghost_y2 + 61), 13)
   
    pygame.draw.circle(screen,eyes_color,(ghost_x2+15, ghost_y2+15), 10)
    pygame.draw.circle(screen,eyes_color,(ghost_x2+16, ghost_y2+18), 10)     
    pygame.draw.circle(screen,eyes_color,(ghost_x2-15, ghost_y2+15), 10)
    pygame.draw.circle(screen,eyes_color,(ghost_x2-13, ghost_y2+12), 10)
    rect = (ghost_x2 -20, ghost_y2 + 30 , 14, 14) 
    pygame.draw.arc(screen, eyes_color,rect, 0, math.pi)
    rect = (ghost_x2 + 10, ghost_y2 + 30 , 14, 14) 
    pygame.draw.arc(screen, eyes_color,rect, 0, math.pi)


    #Decorations
    pygame.draw.circle(screen,(151,89,154),(WIDTH-14, -10),280,25) 
    pygame.draw.circle(screen,(151,89,154),(312, -50),150,25)  
    pygame.draw.circle(screen,"yellow",(WIDTH - 75, -50),200,20) 
    pygame.draw.circle(screen,(232,74,174),(346, -60),150,20)
    pygame.draw.circle(screen,(255,255,255),(-30, -15),260,15) 
    pygame.draw.circle(screen,(255,255,255),(-40, -10),260,15)
    pygame.draw.circle(screen,(255,255,255),(15, -25),200,10) 

    # black frame
    x = 0
    while x <= WIDTH:
        pygame.draw.circle(screen,(0,0,0),(x,5),15)
        x += 20

    x2 = 0
    while x2 <= WIDTH:
            pygame.draw.circle(screen,(0,0,0),(x2,HEIGHT-5),15)
            x2 += 20
    
    y = 0
    while y <= HEIGHT:
        pygame.draw.circle(screen,(0,0,0),(5,y),15)
        y += 20

    y2 = 0
    while y2 <= HEIGHT:
            pygame.draw.circle(screen,(0,0,0),(WIDTH,y2),15)
            y2 += 20

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()