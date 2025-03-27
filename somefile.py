import logging
import time

logger = logging.getLogger(__name__)


def go():
    for _ in range(1, 6):
        time.sleep(1)
        logger.info(f'{time.strftime("%Y-%m-%d %H:%M:%S")}' + f' {_}')

    print('ВСЕ')


print(f"Имя модуля: {__name__}")

if __name__ == "__main__":
    print("Этот файл запущен напрямую.")
else:
    print("Этот файл импортирован как модуль.")
