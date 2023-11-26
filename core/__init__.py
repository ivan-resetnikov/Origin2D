# Import built-in libraries
import logging
import os


# Import external libraries
try: import pygame as pg
except ImportError:
	os.system("pip install pygame-ce")
	import pretty_errors

try: import pretty_errors
except ImportError:
	os.system("pip install pretty-errors")
	import pretty_errors


# Import core libraries
from core.window import Window
from core.scene import Scene
from core.game import Game

import core.sprite_sheet as sprite_sheet
import core.surface as surface
import core.term as term
import core.logging as _



pretty_errors.configure(
	separator_character = '=',
	line_number_first   = True,
	lines_before        = 2,
	lines_after         = 2,
	line_color          = pretty_errors.RED +  "!" + pretty_errors.default_config.line_color + "| " + pretty_errors.RED,
	code_color          = " | " + pretty_errors.GREY,
	truncate_code       = True,
	display_locals      = True
)