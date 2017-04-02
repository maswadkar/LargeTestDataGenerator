# LargeTestDataGenerator
Generate csv files for large data requirement(s)

The input file is \<parameters\> .json
This is the file that controls everything
it has all the required definations. they are defined by keys and values 
keys are 
filename: name of the .csv that will be created 
columns: defination of the columns that will be created in csv file
columns.column_name: column name
columns.datatype: data type of column. It can be <b>string</b> or <b>reference to another column</b> or <b>values in file</b>.
columns.length: legth of the column
columns.is_variable_legth: if the legth can vary or is fixed length. the values is true or false
columns.is_null: is basically is null allowed. if true then length can be 0
columns.file_path: if the datatype is file then, it looks for the values from file in the file_path
separator: is saperator between the columns
number_of_rows: number of rows that should be produced in the file. 
