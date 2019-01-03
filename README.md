# Pandas Simple CSV Parser

Simple CSV parser with the use of the library Pandas for Python for getting specific columns of a CSV file and putting the extracted data into one or more files (each column in a separated file or all of them in the same output).

__Author:__ Levindo Gabriel Taschetto Neto.

## Python Environment

__Python Version:__ Python 3.6.5 :: Anaconda, Inc.

## Pre-Requisites
```
$ conda install pandas
```

## How to Use
```
$ python pandas.py --multipleOutputsBoolean --<SEPARATION_SYMBOL> <INPUT> <[Column Names]> <OUTPUTS_IN_ORDER_OF_COLUMNS>
```

## Examples

In this example, the columns *DS_APRESENTACAO* and *TP_PRODUTO* are extracted from the file [medicines.csv](tests/in/medicines.csv) and placed into the outputs *productNumbers.txt* and *productNames.txt* respectively. As might be obvious, the names of the columns must be specified within the first line of the file, and separated as the presented data.

```
$ python pandas.py --true --; tests/in/medicines.csv [DS_APRESENTACAO TP_PRODUTO] [tests/out/productNumbers.txt tests/out/productNames.txt]
```

## License

MIT License. Click [here](LICENSE.md) for more information about this license.
