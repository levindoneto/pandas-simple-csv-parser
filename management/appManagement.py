import pandas as pd
import management.fileManagement as fileManagement

def run(dataIn, dataOutList, delimiter, listColumns,
        createdQuotedFile, multipleOutputsBoolean):
    '''
    For each requested column, get all the dataframes, and put them (without
    their indexes) in a file without repeated data.
    @param: {str} oldOutput path,\n
            {list} dataOutList paths\n
            {str} delimiter between columns\n
            {list} listColumns\n
            {bool} createdQuotedFile\n
            {bool} multipleOutputsBoolean\n
    @returns: {void}
    '''
    # Create dataframes
    parsedFile = pd.read_csv(dataIn, sep=';', header=None, encoding='utf-8', low_memory=False)

    #Get specific columns from the list of requested ones
    for i in range(len(listColumns)):
        # Get specific column
        savedColumn = parsedFile[listColumns[i]]
        # Remove duplicates
        savedColumn.drop_duplicates(keep = 'first', inplace = True)
        # Put column into a csv
        savedColumn.to_csv(dataOutList[i], sep = '\t', index = False)
        # Quote rows
        fileManagement.createQuotesFile(dataOutList[i], dataOutList[i]+'_quoted')
