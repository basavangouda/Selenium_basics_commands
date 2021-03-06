import logging



#another way
'''logging.basicConfig(filename="test.log",
format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%I %M %S %p',level=logging.DEBUG)

logging.debug('this is debug message')
logging.info('this is info message')
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")'''

#another way

logging.basicConfig(filename="test1.log",
format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%I %M %S %p',level=logging.DEBUG)

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug('this is debug message')
logger.info('this is info message')
logger.warning("this is warning message")
logger.error("this is error message")
logger.critical("this is critical message")
