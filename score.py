import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self, SCORE_FONT_SIZE):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.font = pygame.font.SysFont("Arial", SCORE_FONT_SIZE)
        self.score = 0

    def draw(self, screen):
        text_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text_surface, (0, 0))