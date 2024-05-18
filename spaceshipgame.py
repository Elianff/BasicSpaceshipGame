import pygame
import os #operating system


#constant variables capitalize
WIDTH,HEIGHT = 900,500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GAME")

WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (60,40,190)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)


FPS = 60
VELOCITY = 5
BULLET_VEL = 7
MAX_BULLETS=3
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

YELLOW_HIT=pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90  )


RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270 )



def draw_window(red,yellow,red_bullets, yellow_bullets):
    WINDOW.fill((BLACK))
    pygame.draw.rect(WINDOW,PURPLE,BORDER)
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))   #blit draws surface unto screen
    WINDOW.blit(RED_SPACESHIP, (red.x,red.y))

    for bullet in red_bullets: 
        pygame.draw.rect(WINDOW,RED,bullet)
    
    for bullet in yellow_bullets: 
        pygame.draw.rect(WINDOW,YELLOW,bullet)

    pygame.display.update()

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    clock= pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #makes sure it doesn't go above 60 frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)

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


        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow,red_bullets,yellow_bullets)
    
    pygame.quit()

if __name__ == "__main__":
    main()