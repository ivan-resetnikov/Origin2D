import pygame as pg

import core
import resources



player = None


def init(game: core.Game, scene: core.Scene) -> None:
	scene.fill_color = pg.Color("#222034")
	game
	
	global player
	player = resources.Player()


def update(game: core.Game, scene: core.Scene, delta: float) -> None:
	player.update(scene, delta)


def draw(game: core.Game, scene: core.Scene, window: core.Window) -> None:
	player.draw(window)