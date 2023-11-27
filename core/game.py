import pygame as pg
import logging

from core.scene import Scene
from core.window import Window

import core.input_manager as input_manager



class Game:
	"""
	Class Game controlls game's
	running loop and scene changing
	"""

	def __init__(self):
		self.__window = Window(
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

		self.current_scene.callback_init(self, self.current_scene)

		while self.running:
			input_manager._clear_input_buffer()

			for event in pg.event.get():
				match event.type:
					case pg.QUIT:
						self.running = False

					case pg.KEYDOWN:
						input_manager._add_just_pressed(event.key)

					case pg.KEYUP:
						input_manager._add_just_released(event.key)


			self.__window.surface.fill(self.current_scene.fill_color)

			self.current_scene.callback_update(self, self.current_scene, self.__delta)
			self.current_scene.callback_draw(self, self.current_scene, self.__window)

			pg.display.flip()
			self.__delta = self.__clock.tick(self.fps) * self.__delta_factor

		logging.debug(f"Exit code: {self.exit_code}")
		logging.info("Exiting game")