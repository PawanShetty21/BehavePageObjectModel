import inspect
import logging
import time


class Logger:

    def custom_logger(loglevel=logging.DEBUG):
        # Set class / method name from where it is called
        logger_name = inspect.stack()[1][3]

        # Create logger
        curr_time = time.strftime("%m_%d_%Y_%_H:%_M:%_S").replace(":", "_")
        log_file_name = '../Logs/log' + curr_time + '.txt'
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)

        fh = logging.FileHandler(log_file_name)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # Add formatter to console or file handler
        fh.setFormatter(formatter)

        # Add file handler to logger
        logger.addHandler(fh)
        return logger
