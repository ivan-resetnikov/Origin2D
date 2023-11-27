import core
import pygame as pg

from core.scene import Scene
from core.window import Window



class Player(core.Actor):
	speed: float = 2.0
	friction: float = 0.7

	def __init__(self):
		core.Actor.__init__(self)

		self.sprites: list[pg.Surface] = core.sprite_sheet.load("assets/textures/player.png")

		self.position: pg.math.Vector2 = pg.math.Vector2(250, 250)
		self.velocity: pg.math.Vector2 = pg.math.Vector2(0, 0)

		# Upscale sprites
		for i, sprite in enumerate(self.sprites):
			self.sprites[i] = pg.transform.scale(sprite, (64, 64))


	def ready(self, scene: Scene) -> None:
		pass


	def update(self, scene: Scene, delta: float) -> None:
		keys = pg.key.get_pressed()

		self.velocity += core.input_manager.get_vector(
			pg.K_a, pg.K_d, pg.K_w, pg.K_s) * self.speed

		self.velocity *= self.friction

		self.position += self.velocity


	def draw(self, window: Window) -> None:
		current_sprite: pg.Surface = self.sprites[0]

		window.surface.blit(current_sprite, core.surface.centrify(current_sprite, self.position))