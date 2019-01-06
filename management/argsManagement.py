INTEGER = 0

def getArgList(listString, typeArg):
    import re
    '''
    Get list based on the list of strings passed as
    args parameter
    @param {string} listString\n
           {int} typeArg\n
    @returns {void}
    '''
    columnsList = []
    if (listString[0] != '[' or listString[-1] != ']'):
        return columnsList
    listString = listString[1:-1]
    columnsList = re.sub(",", " ",  listString).split()
    if(typeArg == 0):
        for i in range(len(columnsList)):
            columnsList[i] = int(columnsList[i])
    return columnsList

def getBoolean(boolean):
    return False if boolean == 'false' or boolean == 'False' else True
