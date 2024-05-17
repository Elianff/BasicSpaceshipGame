import pygame


#constant variables capitalize
WIDTH,HEIGHT = 900,500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GAME")

WHITE= (255,255,255)
PURPLE=(60,40,190)

def draw_window():
    WINDOW.fill((PURPLE))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()