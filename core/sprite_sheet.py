import pygame as pg
import logging



MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def load(path: str) -> list[pg.Surface]:
	""" This function extracts images from sprite sheet """

	sprite_sheet = pg.image.load(path).convert()
	sprites = []

	logging.debug(f"Loading spritesheet at \"{path}\"")


	for y in range(sprite_sheet.get_height()):
		for x in range(sprite_sheet.get_width()):
			pixel_color: pg.Color = sprite_sheet.get_at((x, y))

			if pixel_color in (CYAN, MAGENTA):
				width = 1
				height = 1
				transparent = False

				# Check whether is transparent
				if pixel_color == MAGENTA:
					transparent = True

				""" Get width of the sprite by launching a "beam"
				to the right that stops when there is no more
				red (X axis indicator), or on the edge of
				the sprite sheet image """

				pixel_color = RED
				while not (x + width) > sprite_sheet.get_width() - 1 and \
					  pixel_color == RED:

					pixel_color = sprite_sheet.get_at((x + width, y))

					width += 1

				if not pixel_color == RED: width -= 1

				""" Get width of the sprite by launching a "beam"
				down that stops when there is no more
				green (Y axis indicator), or on the edge of
				the sprite sheet image """

				pixel_color = GREEN
				while not (y + height) > sprite_sheet.get_height() - 1 and \
					  pixel_color == GREEN:

					pixel_color = sprite_sheet.get_at((x, y + height))

					height += 1

				if not pixel_color == GREEN: height -= 1

				# Crop sprite from spritesheet
				sprite = sprite_sheet.subsurface((
					x + 1, y + 1,
					width - 1, height - 1))
				
				if transparent:
					sprite.set_colorkey((0, 0, 0))

				sprites.append(sprite)

	logging.debug(f"Loaded {len(sprites)} sprites")

	return sprites