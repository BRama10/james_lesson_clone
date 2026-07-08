# import logging
import helper

from logging import getLogger

from test_folder.cow import wow

# __name__ here is "__main__" because this file is run directly
logger = getLogger(__name__)

def main():
    # Configure logging once, at the entry point.
    # %(name)s prints the logger's name so you can see the difference.
    logging.basicConfig(
        level=logging.INFO,
        format="%(name)s - %(levelname)s - %(message)s",
    )

    logger.info("starting up")
    helper.do_work()
    logger.info("done")

if __name__ == "__main__":
    main()
