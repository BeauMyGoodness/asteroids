import pygame
from constants import *


class ScoreSystem:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def update(self, dt):
        # Add 10 points for every 5 seconds the player is alive
        self.score += (dt / 5.0) * 10

    def asteroid_destroyed(self):
        # Add 200 points when an asteroid is destroyed
        self.score += 200

    def draw(self, screen):
        # Display the score on the screen
        score_text = self.font.render(f"Score: {int(self.score)}", True, "white")
        screen.blit(score_text, (SCREEN_WIDTH / 2, 10))

    def get_score(self):
        return int(self.score)
