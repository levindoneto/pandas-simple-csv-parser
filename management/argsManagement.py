def getColumnsList(listString):
    '''
    Get the columns list based on the list of strings passed as args parameter
    @param {string} listString\n
    @returns {void}
    '''
    columnsList = []
    if (listString[0] != '[' or listString[-1] != ']'):
        return columnsList
    else:
        for i in range(1, len(listString)-1, 2):
            columnsList.append(int(listString[i]))
    return columnsList

def getOutputPaths(listString):
    return []

def getMultipleOutputsBoolean(listString):
    return []
