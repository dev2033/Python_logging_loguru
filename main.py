from loguru import logger

"""
Создаем лог уровня debug,
который обновляется каждый день в 10:00,
архивируя предыдущий лог в zip
"""
logger.add(
	"debug.json",
	format="{time} {level} {message}",
	level="DEBUG",
	rotation="10:00",
	compression="zip",
	# параметр serialize = True позволяет сохранять файл логов в формате JSON
	serialize = True
)

def devide(a, b):
	"""
	Создает с параметрами a и b, где a делиться на b
	"""
	return a / b

"""Декоратор для отслеживания всех исключений в функции main"""
@logger.catch
def main():
	"""Вызывает функцию devide, передавая ей параметры"""
	devide(1, 0)


main()


"""Цикл, который ранжирует лог 1000 раз"""
# for _ in range(1000):
# 	logger.debug("Hello, World(debug)!")
