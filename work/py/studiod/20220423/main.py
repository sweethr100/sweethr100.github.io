import sys
import pygame

def main():
    pygame.font.init()
    pygame.init()
    pygame.display.set_caption("제목")
    dc = pygame.display.set_mode((500,500))
    clock = pygame.time.Clock()
    time = pygame.time.get_ticks()
    while True:
        events = pygame.event.get()
        for event in events:
            if pygame.QUIT == event.type:
                pygame.quit()
                sys.exit(1)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.draw.rect()
            clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    main()