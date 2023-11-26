import pygame as pg



def centrify(surface, position) -> pg.math.Vector2:
	""" Returns centrified position of the sprite,
	here because of redundency. """

	return pg.math.Vector2(
		position[0] - surface.get_width() * 0.5,
		position[1] - surface.get_height() * 0.5)