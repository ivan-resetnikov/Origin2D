import pygame as pg
import logging

from core.window import Window
import core.error as error



class Scene:
	"""
	Class "Scene" is esentially a container
	for game loop functions (init, update, draw),
	with extra setting.
	"""

	def __init__(self,
			callback_init = None,
			callback_update = None,
			callback_draw = None,
			name: str="null",
			fps: int=60
		):

		self.name = name
		self.fill_color = (0, 0, 0)
		self.fps = fps
		
		self.callback_init = callback_init
		self.callback_update = callback_update
		self.callback_draw = callback_draw


	def check_for_errors(self) -> None:
		if not self.callback_init:
			raise AttributeError(error.INIT_CALLBACK_NOT_ASSIGNED)

		if not self.callback_update:
			raise AttributeError(error.UPDATE_CALLBACK_NOT_ASSIGNED)

		if not self.callback_draw:
			raise AttributeError(error.DRAW_CALLBACK_NOT_ASSIGNED)