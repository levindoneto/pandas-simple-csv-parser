import management.appManagement as appManagement

dataIn  = "tests/in/medicines.csv"
dataOut = "tests/out/out.csv"
dataQuotes = "tests/out/quotes.csv"
columnName = 5 #'TP_PRODUTO'
listColumns = []
listColumns.append(5)

appManagement.run(dataIn, dataOut, dataQuotes, ';',
                  listColumns, createdQuotedFile=False)
