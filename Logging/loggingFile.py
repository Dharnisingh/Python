# Program to demonstrate logging module
import logging

print("\nDebug {} \nInfo {} \nWarning {} \nError {} \nCritical {}".format(logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL))

# Writing log to the file
with open('MyLogFile.txt','w') as f:
    print('Loging to file')
    # Configure logger to write to a file
    logging.basicConfig(filename='MyLogFile.txt', level= logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s' )
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.info("I am just an info !!")
    logging.debug("Debug infor!") # Will not be displayed because its value is less than INFO==20
    logging.warning("Hi!")
    logging.error("I am Error!")


