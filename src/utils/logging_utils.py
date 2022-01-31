import logging
import os
import sys

class Logger:
    logger = None

    @staticmethod
    def init_logger():
        Logger.logger = logging.getLogger("ranking_service_logger")
        Logger.logger.setLevel(os.getenv('LOG_LEVEL', 'DEBUG'))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        Logger.logger.addHandler(handler)
