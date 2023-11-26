from dataclasses import dataclass



@dataclass
class fg:
	black = "\033[0;30m"
	white = "\033[0;37m"
	gray = "\033[1;30m"

	red = "\033[0;31m"
	green = "\033[0;32m"
	yellow = "\033[0;33m"
	blue = "\033[0;34m"
	purple = "\033[0;35m"
	cyan = "\033[0;36m"

	reset = "\033[m"