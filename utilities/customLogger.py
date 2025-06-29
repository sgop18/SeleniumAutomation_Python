import logging

# class LogGen:
#
#     @staticmethod
#     def logGeneration():
#         logging.basicConfig(
#             filename="ae_Automation.log",  # log file in current folder
#             filemode='a',                  # append mode
#             format='%(asctime)s - %(levelname)s - %(message)s',
#             datefmt='%m/%d/%Y %I:%M:%S %p',
#             level=logging.INFO
#         )
#         logger = logging.getLogger()
#         return logger
class LogGen:
    @staticmethod
    def logGeneration():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger