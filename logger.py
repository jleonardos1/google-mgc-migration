import logging

class Logger:
    @staticmethod
    def get_logger(name: str, level=logging.INFO):
        logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')
        return logging.getLogger(name)

    @classmethod
    def info(cls, message):
        cls.get_logger(__name__).info(message)

    @classmethod
    def error(cls, message):
        cls.get_logger(__name__).error(message)
