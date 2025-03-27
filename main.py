import logging
import sys
from somefile import go

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    logger.warning('hello epta!')
    go()


if __name__ == '__main__':
    main()
#игорь еблан ничего не делал