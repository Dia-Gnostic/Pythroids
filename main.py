import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pg.init()
	screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pg.time.Clock()
	dt = 0
	updatable = pg.sprite.Group()
	drawable = pg.sprite.Group()
	asteroids = pg.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
	asteroidfield = AsteroidField()



	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				return

		screen.fill("black")

		for object in updatable:
			object.update(dt)
		
		for object in drawable:
			object.draw(screen)

		pg.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
