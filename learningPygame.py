import pygame
from vector import vec, rectAdd
from game import GameEngine
from constants import SCALE


RESOLUTION = vec(800, 800)
UPSCALED = RESOLUTION * SCALE

def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(list(map(int, RESOLUTION)))
    drawSurface = pygame.Surface(list(map(int, RESOLUTION)))

    game = GameEngine()
    

    RUNNING = True
    gameClock = pygame.time.Clock()

    while RUNNING:
        game.draw(drawSurface)

        pygame.transform.scale(drawSurface, RESOLUTION, screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT\
                or (event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE):
                RUNNING = False
            else:
                game.handleEvent(event)
                
        # update world here
        gameClock.tick()
        seconds = gameClock.get_time()/500
        game.update(seconds)

    pygame.quit()

if __name__ == '__main__':
    main()
