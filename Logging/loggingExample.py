# Program to demonstrate logging module
import logging

logging.basicConfig(level=logging.INFO)
logging.info("I am just an info !!")
logging.debug("Debug infor!") # Will not be displayed because its value is less than INFO==20
logging.warning("Hi!")
logging.error("I am Error!")

print("\nDebug {} \nInfo {} \nWarning {} \nError {} \nCritical {}".format(logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL))

# Writing log to the file
with open('MyLogFile.txt','w') as f:
    print('Loging to file')
    logging.basicConfig(filename='MyLogFile.txt', loglevel= logging.DEBUG)
    logging.info("I am just an info !!")
    logging.debug("Debug infor!") # Will not be displayed because its value is less than INFO==20
    logging.warning("Hi!")
    logging.error("I am Error!")


