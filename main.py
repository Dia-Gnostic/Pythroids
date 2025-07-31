import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from player import Player

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pg.init()
	screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pg.time.Clock()
	dt = 0

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				return

		screen.fill("black")
		player.update(PLAYER_TURN_SPEED * dt, PLAYER_SPEED * dt)
		player.draw(screen)
		pg.display.flip()
		dt = clock.tick(60) / 1000
		print(dt)

if __name__ == "__main__":
    main()
