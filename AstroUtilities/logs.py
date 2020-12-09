import logging

def createLogger(log_name, log_level, log_filepath, log_format):
    """
    This function creates a logger object with specific, commonly-usesd params

    Parameters:
        log_name (string): This is the logger's nickname, which may be
            different than the filename
        log_level (string): This sets the logging level (e.g. INFO)
        log_filepath (string): This is the filepath to which the logfile will
            be written and saved to 
        log_format (string): This string determines the format of each entry in
            the output log
    
    Return:
        logging.Logger (object)
    """
    # TODO: add parameter validation
    logger = getLogger(log_name)
    logger.setLevel(str(log_level).upper())

    handler = logging.FileHandler(log_filepath)
    handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(handler)

    return logger

def getLogger(log_name):
    return logging.getLogger(log_name)

