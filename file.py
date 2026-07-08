import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

from functions import add

logger_2 = logging.getLogger(__name__)

logger_2.info('hi')