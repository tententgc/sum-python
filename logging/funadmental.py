import logging 

logging.basicConfig (level= logging.DEBUG , format= '$(asctime)s  - %(name)s -%(levelname)s-%(message)s',datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('This is Debug message')
logging.info("This is info message")
logging.warning("This is Warning message")
logging.error("This is Error message")
logging.critical("This is Critical message")
