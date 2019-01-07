# Pandas Simple CSV Parser

Simple CSV parser for huge volumes of data with the use of the library Pandas for Python for getting specific columns of a CSV file and putting the extracted data into one or more files (each column in a separated file or all of them in the same output) in a short amount of time.

![building](https://travis-ci.com/levindoneto/pandas-simple-csv-parser.svg?branch=master)

__Author:__ Levindo Gabriel Taschetto Neto.

## Python Environment

__Python Version:__ Python 3.6.5 :: Anaconda, Inc.

## Pre-Requisites
```
$ conda install pandas
```

## How to Use
```
$ python pandasParser.py <INPUT> <[COLUMN_NUMBERS(comma-separated)]> <[OUTPUTS_IN_ORDER_OF_COLUMNS(comma-separated)]> <multipleOutputsBoolean> <DELIMITER_SYMBOL> <createQuotedFilesBoolean>
```

## Examples

In this example, the columns *NU_CNPJ* (0) and *NO_PRODUTO* (5) are extracted from the file [medicines.csv](tests/in/medicines.csv) and placed into the outputs *cnpj.csv* and *productNames.csv* respectively.

```
$ python pandasParser.py tests/in/medicines.csv [0,5] [tests/out/cnpj.csv,tests/out/productNames.csv] true ; true
```

## License

MIT License. Click [here](LICENSE.md) for more information about this license.
