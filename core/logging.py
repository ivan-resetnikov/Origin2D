import logging
import datetime
import core.term as term



MESSAGE_SPACE = 40

LOGGING_FORMATS = {
	logging.DEBUG: term.fg.blue + "| {levelname:<8}" + term.fg.reset + " {message:<" + str(MESSAGE_SPACE) + "}",
	logging.INFO: term.fg.green + "| {levelname:<8}" + term.fg.reset + " {message:<" + str(MESSAGE_SPACE) + "}",
	logging.WARNING: term.fg.yellow + "| {levelname:<8}" + term.fg.reset + " {message:<" + str(MESSAGE_SPACE) + "}",
	logging.ERROR: term.fg.red + "| {levelname:<8}" + term.fg.reset + " {message:<" + str(MESSAGE_SPACE) + "}",
	logging.CRITICAL: "\033[1;91m" + "| {levelname:<8}" + term.fg.reset + " {message:<" + str(MESSAGE_SPACE) + "}",
}


class CustomFormatter(logging.Formatter):
	def format(self, record):
		log_format = LOGGING_FORMATS.get(record.levelno)
		formatter = logging.Formatter(log_format, style="{")

		return formatter.format(record)


handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())

logging.basicConfig(
	level=logging.DEBUG,
	handlers=[handler])

time = datetime.datetime.now()

logging.info("Starting logging session {}/{}/{}".format(time.year, time.month, time.day))