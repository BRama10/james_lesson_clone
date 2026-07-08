import logging

# __name__ here is "helper" (the module's import name)
logger = logging.getLogger(__name__)

def do_work():
    logger.info("doing some work")
    logger.warning("something to watch out for")