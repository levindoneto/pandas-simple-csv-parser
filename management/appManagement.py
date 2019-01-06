import pandas as pd
import management.fileManagement as fileManagement

def run(dataIn, dataOut, dataQuotes, delimiter, listColumns, createdQuotedFile):
    '''
    For each requested column, get all the dataframes, and put them (without
    their indexes) in a file without repeated data.
    @param: {str} oldOutput path,\n
            {str} newOutput path\n
            {str} dataQuotes path\n
            {str} delimiter between columns\n
            {list} listColumns\n
            {bool} createdQuotedFile\n
    @returns: {void}
    '''
    # Create dataframes
    parsedFile = pd.read_csv(dataIn,sep = delimiter, header = None,
                             encoding = 'utf-8', low_memory = False)

    # Get specific columns from the list of requested ones
    for i in listColumns:
        savedColumn = parsedFile[i]
        # Remove duplicates
        savedColumn.drop_duplicates(keep = 'first', inplace = True)
        # Put column into a csv
        savedColumn.to_csv(dataOut, sep = '\t', index = False)
        # Quote rows
        fileManagement.createQuotesFile(dataOut, dataQuotes)
