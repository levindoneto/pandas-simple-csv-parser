import pandas as pd

dataIn  = "tests/in/medicines.csv"
dataOut = "tests/out/out.txt"

columnName = 5 #'TP_PRODUTO'

# Create dataframes
parsedFile = pd.read_csv(dataIn, sep=';', header=None, encoding='utf-8', low_memory=False)

# Get specific column
savedColumn = parsedFile[columnName]

# Put column into a csv
savedColumn.to_csv(dataOut, sep='\t', index=False)
