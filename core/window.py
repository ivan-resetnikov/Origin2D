import pygame as pg
import logging



class Window:
	def __init__(self,
			size: list[int]|tuple[int]|pg.math.Vector2=(500, 500),
			title: str="Window",
			icon: str="assets/icon_16x16.png"
		):

		logging.debug(f"Initializing window")
		logging.debug(f" |- Size: {size} {type(size)}")
		logging.debug(f" |- Title: {title} {type(title)}")
		logging.debug(f" '- Icon: {icon} {type(icon)}")

		self.surface = pg.display.set_mode(size)

		pg.display.set_caption(title)
		pg.display.set_icon(pg.image.load(icon))


	def set_title(self, text: str):
		logging.debug(f"Changing window title to \"{text}\"")

		pg.display.set_caption(text)


	def set_icon(self, path: str):
		logging.debug(f"Changing window icon to \"{path}\"")

		pg.display.set_icon(pg.image.load(path))