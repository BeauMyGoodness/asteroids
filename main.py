import pygame
import sys
import random
from constants import *
from logger import *
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        #print(dt)
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        if player.shoot_timer > 0:
            player.shoot_timer -= dt
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("You died! Skill issue?")
                sys.exit()
                return
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()
    

if __name__ == "__main__":
    main()
