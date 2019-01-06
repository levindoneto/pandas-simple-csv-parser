import pandas as pd

dataIn  = "tests/in/medicines.csv"
dataOut = "tests/out/out.csv"
dataQuotes = "tests/out/quotes.csv"
columnName = 5 #'TP_PRODUTO'

def createQuotesFile(oldOutputPath, newOutputPath):
    newOutput = open(newOutputPath, 'w', encoding="utf8");
    with open(oldOutputPath, 'r', encoding="utf8") as f:
        lines = f.read().splitlines()
        for i in lines:
            newOutput.write('"'+str(i)+'",\n')


# Create dataframes
parsedFile = pd.read_csv(dataIn, sep=';', header=None, encoding='utf-8', low_memory=False)

# Get specific column
savedColumn = parsedFile[columnName]

# Remove duplicates
savedColumn.drop_duplicates(keep='first', inplace=True)

# Put column into a csv
savedColumn.to_csv(dataOut, sep='\t', index=False)

# Quote rows
createQuotesFile(dataOut, dataQuotes)
