import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fight Crime Or Sum Like That")

goober = pygame.image.load("goober.png")  
goober = pygame.transform.scale(goober, (100, 100))


background = (0, 0, 0)



size = 100
xCord = WIDTH / 2
yCord = HEIGHT / 2
speed = 5


clock = pygame.time.Clock()


running = True
while running:
    screen.fill(background)  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    actions = pygame.key.get_pressed()
    if actions[pygame.K_LEFT] or actions[pygame.K_a]:
        xCord -= speed  
    if actions[pygame.K_RIGHT] or actions[pygame.K_d]:
        xCord += speed  
    if actions[pygame.K_UP] or actions[pygame.K_w]:
        yCord -= speed  
    if actions[pygame.K_DOWN] or actions[pygame.K_s]:
        yCord += speed  

    
    xCord = max(0, min(WIDTH - size, xCord))
    yCord = max(0, min(HEIGHT - size, yCord))

    
    screen.blit(goober, (xCord, yCord))

    
    pygame.display.flip()

    
    clock.tick(60)