import pandas as pd

dataIn  = "tests/in/medicines.csv"

dataOut = open("tests/out/out.txt", "w")

columnName = 5 #'TP_PRODUTO'

parsedFile = pd.read_csv(dataIn, sep=';', header=None, encoding='utf-8', low_memory=False)

savedColumn = parsedFile[columnName]

print(savedColumn)
