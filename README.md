# LargeTestDataGenerator
Generate csv files for large data requirement(s)
<br>The input file is \<parameters\> .json
<br>This is the file that controls everything
<br>it has all the required definations. they are defined by keys and values 
<br>keys are 
<br>filename: name of the .csv that will be created 
<br>columns: defination of the columns that will be created in csv file
<br>columns.column_name: column name
<br>columns.datatype: data type of column. It can be <b>string</b> or <b>reference to another column</b> or <b>values in file</b>.
<br>columns.length: legth of the column
<br>columns.is_variable_legth: if the legth can vary or is fixed length. the values is true or false
<br>columns.is_null: is basically is null allowed. if true then length can be 0
<br>columns.file_path: if the datatype is file then, it looks for the values from file in the file_path
<br>separator: is saperator between the columns
<br>number_of_rows: number of rows that should be produced in the file. 
