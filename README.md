# LargeTestDataGenerator
Generate csv files for large data requirement(s)
<br>The input file is \<parameters\> .json
<br>This is the file that controls everything
<br>it has all the required definations. they are defined by keys and values 
<br>keys are mentioned below
<br> <i>filename: </i>name of the .csv that will be created 
<br> <i>columns: </i>defination of the columns that will be created in csv file
<br> <i>columns.column_name: </i>column name
<br> <i>columns.datatype: </i>data type of column. It can be <b>string</b> or <b>reference to another column</b> or <b>values in file</b>.
<br> <i>columns.length: </i>legth of the column
<br> <i>columns.is_variable_legth: </i>if the legth can vary or is fixed length. the values is true or false
<br> <i>columns.is_null: </i>is basically is null allowed. if true then length can be 0
<br> <i>columns.file_path: </i>if the datatype is file then, it looks for the values from file in the file_path
<br> <i>separator: </i>is saperator between the columns
<br> <i>number_of_rows:</i>number of rows that should be produced in the file. 
