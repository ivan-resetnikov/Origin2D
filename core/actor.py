import logging

from core.scene import Scene
from core.window import Window



class Actor:
	def __init__(self) -> None:
		logging.debug(f"Initializing new actor {str(self)}")
		

	def ready(self, scene: Scene) -> None:
		pass


	def update(self, scene: Scene, delta: float) -> None:
		pass


	def draw(self, window: Window) -> None:
		pass