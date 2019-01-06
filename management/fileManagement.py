def createQuotesFile(oldOutputPath, newOutputPath):
    '''
    Replace each row of the file located in _oldOutputPath_ for the same line
    enclosed with quotes, and each \n for \n with a comma aside.
    @param: {str} oldOutputPath,\n
            {str} newOutputPath\n
    @returns: {void}
    '''
    newOutput = open(newOutputPath, 'w', encoding = 'utf8');
    with open(oldOutputPath, 'r', encoding = 'utf8') as f:
        lines = f.read().splitlines() # readlines() without breaking the lines
        for i in lines:
            newOutput.write('"' + str(i) + '",\n')
