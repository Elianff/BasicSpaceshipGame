import pygame
import os #operating system


#constant variables capitalize
WIDTH,HEIGHT = 900,500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GAME")

WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (60,40,190)

BORDER = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)


FPS = 60
VELOCITY = 5
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90  )


RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270 )



def draw_window(red,yellow):
    WINDOW.fill((PURPLE))
    pygame.draw.rect(WINDOW,BLACK,BORDER)
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))   #blit draws surface unto screen
    WINDOW.blit(RED_SPACESHIP, (red.x,red.y))
    pygame.display.update()
    

def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)


    clock= pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #makes sure it doesn't go above 60 frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0 : #LEFT
            yellow.x -= VELOCITY
        if keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width< BORDER.x: #RIGHT
            yellow.x += VELOCITY
        if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0 : #UP
            yellow.y -= VELOCITY
        if keys_pressed[pygame.K_s] and yellow.y + VELOCITY +yellow.height < HEIGHT - 15 : #DOWN
            yellow.y += VELOCITY


        if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x + BORDER.width: #LEFT
            red.x -= VELOCITY
        if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH: #RIGHT
            red.x += VELOCITY
        if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0 : #UP
            red.y -= VELOCITY
        if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY +red.height < HEIGHT - 15 : #DOWN
            red.y += VELOCITY
        draw_window(red,yellow)
    
    pygame.quit()

if __name__ == "__main__":
    main()