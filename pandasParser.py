'''
Usage:
    python pandasParser.py <INPUT> <[COLUMN_NUMBERS(comma-separated)]> <[OUTPUTS_IN_ORDER_OF_COLUMNS(comma-separated)]> <multipleOutputsBoolean> <DELIMITER_SYMBOL> <createQuotedFilesBoolean>
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

INTEGER = 0
STRING  = 1

def main(args):
    try:
        dataIn = args[1]
        listColumns = argsManagement.getArgList(args[2], INTEGER)
        dataOut = argsManagement.getArgList(args[3], STRING)
        multipleOutputsBoolean = argsManagement.getBoolean(args[4])
        delimiter = args[5]
        createdQuotedFiles = argsManagement.getBoolean(args[6])

        appManagement.run(dataIn, dataOut, delimiter, listColumns,
                          createdQuotedFiles, multipleOutputsBoolean)
    except Exception as e:
        logging.error('[Error]: Invalid list of arguments\n' + str(e))
        logging.error('%s', traceback.format_exc() + '\n')
        logging.info('Correct way to use args:')
        logging.info('python pandasParser.py <INPUT> <[COLUMN_NUMBERS(comma-separated)]>\
                     <[OUTPUTS_IN_ORDER_OF_COLUMNS(comma-separated)]> multipleOutputsBoolean\
                     <DELIMITER_SYMBOL> <CREATE_QUOTED>')

if __name__ == '__main__':
    main(sys.argv)
