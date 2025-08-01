import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        randomangle = random.uniform(20, 50)
        A = Asteroid(*self.position, self.radius - ASTEROID_MIN_RADIUS)
        B = Asteroid(*self.position, self.radius - ASTEROID_MIN_RADIUS)
        A.velocity = self.velocity.rotate(randomangle) * 1.2
        B.velocity = self.velocity.rotate(-randomangle) * 1.2