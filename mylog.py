import logging


def init_loggin(name: str, log_file: str = "dir_stat.log") -> logging.Logger:
    FORMAT = "{levelname:<6} - {asctime}. {msg}"
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(filename=log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(FORMAT, style="{"))
    logger.addHandler(file_handler)

    return logger
