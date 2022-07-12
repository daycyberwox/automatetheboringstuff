# Set up logging in python
 

# Prerequsites
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Send logs to file with prerequisites
# import logging
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# disable all the logging after testing
logging.disable(logging.CRITICAL)


# log messages
logging.debug('Start of program')

# intentionally buggy code
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range (1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))