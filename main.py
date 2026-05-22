import pygame
from player import Player
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    klok = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    AsteroidField()
    
    while True:
        updatable.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            else:
                pass
        log_state()
        
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        tiking = klok.tick(60)
        dt = tiking / 1000

if __name__ == "__main__":
    main()