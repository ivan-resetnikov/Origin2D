import core
import scenes



if __name__ == "__main__":
	main_scene = core.Scene(
		callback_init=scenes.main_menu.init,
		callback_update=scenes.main_menu.update,
		callback_draw=scenes.main_menu.draw,
		name="main_scene")

	game = core.Game()
	game.change_scene(main_scene)
	game.run()