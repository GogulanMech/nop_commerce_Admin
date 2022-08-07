import logging

class loggen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="automation.log",format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%M/%d/%y %h:%m:%s %a')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger



