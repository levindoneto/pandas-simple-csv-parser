'''
Usage:
    python pandasParser.py <INPUT> <[Column Numbers]> <[OUTPUTS_IN_ORDER_OF_COLUMNS]> -multipleOutputsBoolean -<DELIMITER_SYMBOL>
Options:
  -n INT                          The n used to get n-gram probabilities
  -s <path>, --save_model <path>  The path to save the model to
  -l <path>, --load_model <path>  The path to load the model from
'''

import management.appManagement as appManagement
import management.argsManagement as argsManagement
import sys
import traceback
import logging

#a = "tests/in/medicines.csv"
dataOut = "tests/out/out.csv"
dataQuotes = "tests/out/quotes.csv"
columnName = 5 #'TP_PRODUTO'
listColumns = []
listColumns.append(5)

# appManagement.run(dataIn, dataOut, dataQuotes, ';',
#                   listColumns, createdQuotedFile = False)

def main(args):
    try:
        dataIn = args[1]
        listColumns = argsManagement.getColumnsList(args[2])
        print(listColumns)
        dataOut = argsManagement.getOutputPaths(args[3])
        multipleOutputsBoolean = argsManagement.getMultipleOutputsBoolean(args[4])
        multipleOutputsBoolean = args[5]
    except Exception as e:
        logging.error('[Error]: Invalid list of arguments\n' + str(e))
        logging.error('%s', traceback.format_exc() + '\n')
        logging.info('Correct way to use args:')
        logging.info('python pandasParser.py <INPUT> <[COLUMN_NUMBERS(comma-separated)]>\
        <[OUTPUTS_IN_ORDER_OF_COLUMNS(comma-separated)]> -multipleOutputsBoolean DELIMITER_SYMBOL>')

if __name__ == '__main__':
    main(sys.argv)
