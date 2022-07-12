# Raise statement without stopping or crashing a program

import traceback

# store errors in an error_log.txt file

try:
    raise Exception("This is an error message.")
except:
    errorFile = open('error_log.txt', 'a') # create a new error_log.txt file and open it in append mode
    errorFile.write(traceback.format_exc())
    errorFile.close
    print('The traceback info was written to error_log.txt')