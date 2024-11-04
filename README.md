# Pqc Test Python Script

## Command

Run this script with the following command.

```shell
python3 main.py <input_file> <output_file>
```

To get the output flag types and subtypes in their text form add the **text** flag.

```shell
python3 main.py <input_file> <output_file> --text
```

## Input file

Example **input.csv**:

```csv
CompanyNumber
00004606
00015129
```

## Output file

Example **output.csv**:

```csv
CompanyNumber,Type,Subtype,Result
00004606,1,1,True
00004606,1,2,False
00004606,1,3,False
00004606,2,1,False
00004606,2,2,False
00004606,2,3,True
00004606,2,4,False
00004606,2,5,False
00004606,3,1,False
00004606,3,2,False
00004606,3,3,False
```

Example **output.csv** with **text** flag:

```csv
CompanyNumber,Type,Subtype,Result
00004606,Associated Business,Associated Business Insolvency,False
00004606,Associated Business,HM Court Data,False
00004606,Associated Business,Charges on other businesses,False
00004606,Business,CCJ (Business),False
00004606,Business,Director resignations,False
00004606,Business,Accounts Overdue,False
00004606,Business,Incorporation Date,False
00004606,Business,Adverse SIC Code,False
```
