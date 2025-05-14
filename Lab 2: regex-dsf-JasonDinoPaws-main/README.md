# Lab 2: Regular Expressions

## Adding User Accounts
A client just sent over a list of email addresses(`emails.txt`) to your business and you are responsible for creating their user accounts. Each account will need a username and password that is generated from components of their email address. 

### Your Task
Validate the email addresses are in the format `firstname_lastname@dept.company.com`. Then, create a username for each using the format `Flastname#-dept`where `F` represents their first initial capitalized and  `#` represents an optional number to prevent duplicates. For example, if `Jdoe-sales` is already in use and you need to create an user for `jane_doe@sales.yahoo.com` the new user would be `Jdoe2-sales`. Next, generate a password for each user in the format `Flastname########` where `#` represents a random digit 0-9. Output the newly generated accounts in a CSV file `accounts.csv` with each account on a new line in the following format `email,username,password`.
#### Example
| `emails.txt` | `accounts.csv` |
|---|---|
| jane_doe@sales.yahoo.com | jane_doe@sales.yahoo.com,Jdoe-sales,Jdoe87361529 |
| jake_doe@sales.yahoo.com | jake_doe@sales.yahoo.com,Jdoe2-sales,Jdoe093746263 |
| taylor_smith@marketing.yahoo.com | taylor_smith@marketing.yahoo.com,Tsmith-marketing,Tsmith18364950 | 

## Preventing SQL Injections
When you enter your login credentials,  your computer needs to check whether that username and password combination has been registered. One way to store this information would be in a SQL database. If a user entered a SQL command instead of their username/password, its possible this command could be executed on the database and sensitive information could be exposed. This type of attack is called an SQL injection. Login information is not stored in plaintext(hopefully!) but you can see how important it is to clean user input to maintain a secure site. Luckily SQL injections are able to be prevented by filtering since SQL command follow an identifiable format.  For this lab, you will check user input for potential SQL injections using regular expressions. 

### A Little SQL
SQL is a language used to interact with databases. Each database contains one or more tables with named columns that store records(rows) of data. Think any data table you have made in science class before. Most of the actions you need to interact with databases are SQL statements consisting of keywords.

For example, to get all the data from a table in SQL, you use the command `SELECT * FROM TableName;` The `*` is a wildcard character, representing every column. So, this command gets every column from the table `TableName`. You can continue to modify this basic command by adding more keywords to the statement. For example `SELECT * FROM Customers WHERE Country='Mexico';` or `SELECT * FROM Customers WHERE Country = 'Germany' OR Country = 'Spain';`. 

Since each of these statements follow a recognizable pattern, starting with `SELECT` and ending with `;`, we can filter these out from user input using regular expressions! 

### Your Task
You will write a program to read in the files `regex_input1.txt` and `regex_input2.txt` and check all of the lines for potential SQL injections. Remove the SQL statement text and replace it with `[COMMAND DETECTED]`.  After reading through the file, print either `Success!` or `SQL Injection Detected! User tried to input [PUT THE COMMAND HERE], [NEXT COMMAND HERE], etc.`
