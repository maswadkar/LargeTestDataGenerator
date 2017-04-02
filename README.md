# LargeTestDataGenerator
Generate csv files for large data requirement(s)

The input file is <parameters>.json
This is the file that controls everything
it has all the required definations. they are defined by keys and values 
keys are 
filename: name of the .csv that will be created 
columns: defination of the columns that will be created in csv file
columns.column_name: column name
columns.datatype: data type of column. It can be string or reference to another column or values in file.
