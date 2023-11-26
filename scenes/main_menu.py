import core
import pygame as pg



sprites = []


def init(scene) -> None:
	scene.fill_color = pg.Color("#222034")

	global sprites
	sprites = core.sprite_sheet.load("assets/textures/test_sprite_sheet.png")

	sprites[0] = pg.transform.scale(sprites[0], (128, 128))
	sprites[1] = pg.transform.scale(sprites[1], (128, 128))


def update(scene: core.Scene, delta: float) -> None:
	pass


def draw(scene: core.Scene, window: core.Window) -> None:
	window.surface.blit(sprites[0], core.surface.centrify(sprites[0], (250-64, 250)))
	window.surface.blit(sprites[1], core.surface.centrify(sprites[1], (250+64, 250)))