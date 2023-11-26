import pygame as pg
import logging

from core.scene import Scene
from core.window import Window



class Game:
	"""
	Class Game controlls game's
	running loop and scene changing
	"""

	def __init__(self):
		self.window = Window(
			size=(500, 500),
			title="Window")

		self.__clock = pg.time.Clock()
		self.__delta = 1
		self.__delta_factor = 1

		self.running = True
		self.fps = 60

		self.current_scene = None
		self.exit_code = 0


	def change_scene(self, target_scene: Scene) -> None:
		logging.debug(f"Loading scene \"{target_scene.name}\"")

		target_scene.check_for_errors()
		
		self.current_scene = target_scene


	def update_delta(self) -> None:
		""" Recalculates delta miltiplier,
		because doing so at runtime is slow. """

		self.__delta_milti = 1 / 17 * (self.fps / 60)


	def run(self) -> None:
		logging.info("Starting game")

		self.current_scene.callback_init(self.current_scene)

		while self.running:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.running = False

			self.window.surface.fill(self.current_scene.fill_color)

			self.current_scene.callback_update(self.current_scene, self.__delta)
			self.current_scene.callback_draw(self.current_scene, self.window)

			pg.display.flip()
			self.__delta = self.__clock.tick(self.fps) * self.__delta_factor

		logging.debug(f"Exit code: {self.exit_code}")
		logging.info("Exiting game")