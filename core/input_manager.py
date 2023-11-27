import pygame as pg



_just_pressed: list[int] = []
_just_released: list[int] = []


def get_vector(negative_x, positive_x, negative_y, positive_y) -> pg.math.Vector2:
	vector: pg.math.Vector2 = pg.math.Vector2(0, 0)

	pressed = pg.key.get_pressed()
	if pressed[negative_x]: vector.x -= 1
	if pressed[positive_x]: vector.x += 1
	if pressed[negative_y]: vector.y -= 1
	if pressed[positive_y]: vector.y += 1

	return vector


def get_axis(negative, positive) -> int:
	axis: int = 0

	pressed = pg.key.get_pressed()
	if pressed[negative]: axis -= 1
	if pressed[positive]: axis += 1

	return axis


def is_key_just_pressed(key: int) -> bool:
	return key in _just_pressed


def is_key_just_released(key: int) -> bool:
	return key in _just_released


def _clear_input_buffer() -> None:
	_just_pressed.clear()
	_just_released.clear()


def _add_just_pressed(key: int) -> None:
	_just_pressed.append(key)


def _add_just_released(key: int) -> None:
	_just_released.append(key)