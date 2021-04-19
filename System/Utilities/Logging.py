import logging
from os import listdir, mkdir, path, remove

from System.Config import LoggingConfig


def initialize_logs() -> None:
    """
    This function initializes the system and telemetry logs for the run, to include ensuring the chosen directory exists
    and cleaning the directory of its current contents
    :return: None
    """
    # Check for destination directory's existence and clean it out
    if not path.exists(LoggingConfig.DIR):
        mkdir(LoggingConfig.DIR)
    else:
        for file in listdir(LoggingConfig.DIR):
            remove(path.join(LoggingConfig.DIR, file))

    # Initialize system logs
    file_handler = logging.FileHandler(path.join(LoggingConfig.DIR, LoggingConfig.SYSTEM.FILENAME))
    file_handler.setLevel(LoggingConfig.LEVEL)
    file_handler.setFormatter(logging.Formatter(LoggingConfig.SYSTEM.FORMATTER))

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LoggingConfig.LEVEL)
    console_handler.setFormatter(logging.Formatter(LoggingConfig.SYSTEM.FORMATTER))

    system_logger = logging.getLogger(LoggingConfig.SYSTEM.NAME)
    system_logger.setLevel(LoggingConfig.LEVEL)
    system_logger.addHandler(file_handler)
    system_logger.addHandler(console_handler)
    del file_handler, console_handler

    # Initialize telemetry logs
    file_handler = logging.FileHandler(path.join(LoggingConfig.DIR, LoggingConfig.TELEMETRY.FILENAME))
    file_handler.setLevel(LoggingConfig.LEVEL)
    file_handler.setFormatter(logging.Formatter(LoggingConfig.TELEMETRY.FORMATTER))

    telemetry_logger = logging.getLogger(LoggingConfig.TELEMETRY.NAME)
    telemetry_logger.setLevel(LoggingConfig.LEVEL)
    telemetry_logger.addHandler(file_handler)
    del file_handler


def get_system_logger() -> logging.Logger:
    return logging.getLogger(LoggingConfig.SYSTEM.NAME)


def get_telemetry_logger() -> logging.Logger:
    return logging.getLogger(LoggingConfig.TELEMETRY.NAME)
