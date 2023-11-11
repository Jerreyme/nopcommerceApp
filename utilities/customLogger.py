import logging


#class LogGen:
#    @staticmethod
#    def loggen():
#        logging.basicConfig(filename=".\\Logs\\automation.log",
#                            format='%(asctime)s: %(levelname)s: %message)s',
#                            datefmt='%m/%d/%Y %I:%M:%S %p')
#        logger = logging.getLogger()
#        logger.setLevel(logging.INFO)
#       return logger

#Solution 1:

#class LogGen:
#    @staticmethod
#        logger = logging.getLogger()
#        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
#        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#        fhandler.setFormatter(formatter)
#        logger.addHandler(fhandler)
#        logger.setLevel(logging.INFO)
#        return logger

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler = logging.FileHandler(filename=".\\Logs\\automation1.log")
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
# With this sentence i can print the message type INFO, ERROR and WARNING
# logger.setLevel(logging.DEBUG) # If we want to logged the bug type sentences from the console then we can show them with this line (its a lot of lines)
        logger.info("-----> Execution of TC")
        return logger

