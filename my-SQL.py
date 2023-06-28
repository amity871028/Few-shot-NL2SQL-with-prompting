instruction = """
To make the SQL generation process of the text-to-sql task smoother, I will teach you SQL normalization step by step.

"""

# from wiki, 但後面table舉例怪怪的，所以先暫停不用這個例子
tmp = """
# Through the database regularization process, learn how to write SQL query
The normal forms (from least normalized to most normalized) are: UNF(Unnormalized form), 1NF(First normal form), 2NF(Second normal form), 3NF(Third normal form), EKNF(Elementary key normal form), BCNF(Boyce–Codd normal form), 4NF(Fourth normal form), ETNF(Essential tuple normal form), 5NF(Fifth normal form), DKNF(Domain-key normal form), 6NF(Sixth normal form.
Now, we have an initial data:
Table xxxxxxxxx, column = [*,ISBN,Title,Author,Author_Nationality,Format,Price,Subject,Pages,Thickness,Publisher,Publisher_Country,Publication_Type,Genre_ID,Genre_Name]
Table xxxxxxxxx, cell value = [{ISBN:1590593324,Title:Beginning MySQL Database Design and Optimization,Author:Chad Russell,Author_Nationality:American,Format:Hardcover,Price:49.99,Subject:MySQL|Database|Design,Pages:520,Thickness:Thick,Publisher:Apress,Publisher_Country:USA,Publication_Type:E-book,Genre_ID:1, Genre_Name:Tutorial}]
Q: I want to know
SQL: SELECT .....

To satisfy 1NF, each column of a table must have a single value. Columns which contain sets of values or nested records are not allowed. In the initial table, Subject contains a set of subject values, meaning it does not comply.
To solve the problem, the subjects are extracted into a separate Subject table.
## After 1NF, new table:
Table Book, column = [*,ISBN,Title,Author,Author_Nationality,Format,Price,Pages,Thickness,Publisher,Publisher_Country,Publication_Type,Genre_ID,Genre_Name]
Table Book, primary_keys = [Title,Format]
Table Subject, column = [*, ISBN, Subject_name]
Table Subject, primary_keys = [ISBN]
Foreign_keys = [Book.ISBN = Subject.ISBN]
Table Book, cell value = [{ISBN:1590593324,Title:Beginning MySQL Database Design and Optimization,Author:Chad Russell,Author_Nationality:American,Format:Hardcover,Price:49.99,Pages:520,Thickness:Thick,Publisher:Apress,Publisher_Country:USA,Publication_Type:E-book,Genre_ID:1, Genre_Name:Tutorial}]
Table Subject, cell value = [{ISBN:1590593324,Subject_name:MySQL},{ISBN:1590593324,Subject_name:Database},{ISBN:1590593324,Subject_name:Design},]
Q: I want to .......
SQL: SELECT .........

To satisfy 2NF, a table can not has a multi-column or composite key. The Book table has a composite key of [Title, Format]. At this point in our design the key is not finalised as the primary key, so it is called a candidate key.

"""

# 例子 from 以下連結
# https://ithelp.ithome.com.tw/articles/10229472
sql_norm = """
# Through the database regularization process, learn how to write SQL query
The normal forms (from least normalized to most normalized) are: UNF(Unnormalized form), 1NF(First normal form), 2NF(Second normal form).
Now, we have an initial data(UNF data):
Table Comsumptions, columns = [*,Name,Sex,Gender,Item,Price,Quantity,Store,Address,Date,Order_Number]
Table Comsumptions, cell_values = [{Name:Lily,Sex:Female,Gender:F,Item:pensil|eraser,Price:20|50,Quantity:1|2,Store:A store,Address:University Road,Date:12/17,Order_Number:1},{Name:Amy,Sex:Female,Gender:F,Item:milk|sandwish,Price:70|10,Quantity:3|1,Store:B store,Address:Beimen Road,Date:12/18,Order_Number:2},{Name:Amy,Sex:Female,Gender:F,Item:milk|sandwish,Price:70|10,Quantity:3|4,Store:B store,Address:Beimen Road,Date:12/19,Order_Number:3},{Name:David,Sex:Male,Gender:M,Item:omelette|milk tea,Price:30|40,Quantity:1|2,Store:C store,Address:Chenggong Road,Date:12/19,Order_Number:4}]
## Text-to-SQL example:
Q: What did Lily buy on 12/17?
SQL: SELECT Item FROM Comsumptions WHERE Name = 'Lily' and Date = '12/17' 

To satisfy 1NF, we need to follow:
1) each column of a table must have a single value.
2) Columns which contain sets of values or nested records are not allowed.
3) each table requires at least one primary key.
In the initial table, Item and Quantity contain multiple values. Sex and Gender have the same meaning. In the table, there is no primary key.
## Based on 1NF, the new table:
Table Comsumptions, columns = [*,Name,Sex,Item,Price,Quantity,Total_Amount,Store,Address,Date,Order_Number]
Table Comsumptions, primary_keys = [Name,Item,Quantity,Store,Date,Order_Number]
Table Comsumptions, cell_values = [{Name:Lily,Sex:Female,Item:pensil,Price:20,Quantity:1,Total_Amount:20,Store:A store,Address:University Road,Date:12/17,Order_Number:1},{Name:Lily,Sex:Female,Item:eraser,Price:50,Quantity:2,Total_Amount:100,Store:A store,Address:University Road,Date:12/17,Order_Number:1},{Name:Amy,Sex:Female,Item:milk,Price:70,Quantity:3,Total_Amount:140,Store:B store,Address:Beimen Road,Date:12/18,Order_Number:2},{Name:Amy,Sex:Female,Item:sandwish,Price:10,Quantity:1,Total_Amount:10,Store:B store,Address:Beimen Road,Date:12/18,Order_Number:2},{Name:Amy,Sex:Female,Item:milk,Price:70,Quantity:3,Total_Amount:210,Store:B store,Address:Beimen Road,Date:12/19,Order_Number:3},{Name:Amy,Sex:Female,Item:sandwish,Price:10,Quantity:4,Total_Amount:40,Store:B store,Address:Beimen Road,Date:12/19,Order_Number:3},{Name:David,Sex:Male,Item:omelette,Price:30,Quantity:1,Total_Amount:30,Store:C store,Address:Chenggong Road,Date:12/19,Order_Number:4},{Name:David,Sex:Male,Item:milk tea,Price:40,Quantity:2,Total_Amount:80,Store:C store,Address:Chenggong Road,Date:12/19,Order_Number:4}]
## Text-to-SQL example:
Q: What did Lily buy on 12/17?
SQL: SELECT Item FROM Comsumptions WHERE Name = 'Lily' and Date = '12/17' 

Q: How much did Amy spend on 12/19?
SQL: SELECT SUM(*) FROM Comsumptions WHERE Name='Amy' and Date = '12/19'

To satisfy 2NF, we need to follow:
1) Single column primary Key does not functionally dependant on any subset of candidate key relation.
In the 1NF table, every consumption record records the gender of the consumer, the name and address of the store, and there are too many duplicates.
## Based on 2NF, the new table:
Table Consumers, columns = [*,Id,Name,Sex]
Table Consumers, primary_keys = [Id]
Table Consumers, cell_values = [{Id:2,Name:Lily,Sex:Female,Id:3,Name:Amy,Sex:Female,Id:4,Name:David,Sex:Male}]
Table Shops, columns = [*,Id,Store,Address]
Table Shops, primary_keys = [Id]
Table Shops, cell_values = [{Id:1,Store:A store,Address:University Road,Id:2,Store:B store,Address:Beimen Road,Id:3,Store:C store,Address:Chenggong Road}]
Table Items, columns = [*,Id,Item,Price,Store_Id]
Table Items, primary_keys = [Id]
Table Items, cell_values = [{Id:1,Item:pensil,Price:20,Store_Id:1},{Id:2,Item:eraser,Price:50,Store_Id:1},{Id:3,Item:milk,Price:70,Store_Id:2},{Id:4,Item:sandwish,Price:10,Store_Id:2},{Id:5,Item:omelette,Price:30,Store_Id:3},{Id:6,Item:milk tea,Price:40,Store_Id:3}]
Table Orders, columns = [*,Id,Consumer_Id,Item_Id,Quantity,Total_Amount,Date,Order_Number]
Table Orders, primary_keys = [Id]
Table Orders, cell_values = [{Id:1,Consumer_Id:1,Item_Id:1,Quantity:1,Total_Amount:20,Date:12/17,Order_Number:1},{Id:2,Consumer_Id:1,Item_Id:2,Quantity:2,Total_Amount:100,Date:12/17,Order_Number:1},{Id:3,Consumer_Id:2,Item_Id:3,Quantity:3,Total_Amount:210,Date:12/18,Order_Number:2},{Id:4,Consumer_Id:2,Item_Id:4,Quantity:1,Total_Amount:10,Date:12/18,Order_Number:2},{Id:5,Consumer_Id:2,Item_Id:3,Quantity:3,Total_Amount:210,Date:12/19,Order_Number:3},{Id:6,Consumer_Id:2,Item_Id:4,Quantity:4,Total_Amount:40,Date:12/19,Order_Number:3},{Id:7,Consumer_Id:3,Item_Id:5,Quantity:1,Total_Amount:30,Date:12/19,Order_Number:4},{Id:8,Consumer_Id:3,Item_Id:6,Quantity:2,Total_Amount:80,Date:12/19,Order_Number:4}]
## Text-to-SQL example:
Q: What did Lily buy on 12/17?
SQL: SELECT Item FROM Items JOIN Orders ON Items.Id = Orders.Item_Id JOIN Consumers ON Consumers.Id = Orders.Consumer_Id WHERE Consumers.Name = 'Lily' and Orders.Date = '12/17' 

Q: How much did Amy spend on 12/19?
SQL: SELECT SUM(Total_Amount) FROM Orders JOIN Consumers ON Orders.Consumer_Id = Consumers.Id WHERE Consumers.Name = 'Amy' AND Date = '12/19'

"""

sql_norm_del_value = """
# Through the database regularization process, learn how to write SQL query
The normal forms (from least normalized to most normalized) are: UNF(Unnormalized form), 1NF(First normal form), 2NF(Second normal form), 3NF(Third normal form).
Now, we have an initial data(UNF data):
Table Comsumptions, columns = [*,Name,Sex,Gender,Item,Price,Quantity,Store,Date,Order_Number]
## Text-to-SQL example:
Q: What did Lily buy on 12/17?
SQL: SELECT Item FROM Comsumptions WHERE Name = 'Lily' and Date = '12/17' 

To satisfy 1NF, we need to follow:
1) each column of a table must have a single value.
2) Columns which contain sets of values or nested records are not allowed.
3) each table requires at least one primary key.
In the initial table, Item and Quantity contain multiple values. Sex and Gender have the same meaning. In the table, there is no primary key.
## Based on 1NF, the new table:
Table Comsumptions, columns = [*,Name,Sex,Item,Price,Quantity,Total_Amount,Store,Date,Order_Number]
Table Comsumptions, primary_keys = [Name,Item,Quantity,Store,Date,Order_Number]
# Text-to-SQL example:
Q: What did Lily buy on 12/17?
SQL: SELECT Item FROM Comsumptions WHERE Name = 'Lily' and Date = '12/17' 

Q: How much did Amy spend on 12/19?
SQL: SELECT SUM(*) FROM Comsumptions WHERE Name='Amy' and Date = '12/19'

To satisfy 2NF, we need to follow:
1) Single column primary Key does not functionally dependant on any subset of candidate key relation.
In the 1NF table, every consumption record records the gender of the consumer, the name of the store, and there are too many duplicates.
## Based on 2NF, the new table:
Table Consumers, columns = [*,Id,Name,Sex]
Table Consumers, primary_keys = [Id]
Table Shops, columns = [*,Id,Store]
Table Shops, primary_keys = [Id]
Table Items, columns = [*,Id,Item,Price,Store_Id]
Table Items, primary_keys = [Id]
Table Orders, columns = [*,Id,Consumer_Id,Item_Id,Quantity,Total_Amount,Date,Order_Number]
Table Orders, primary_keys = [Id]
## Text-to-SQL example:
Q: What did Lily buy on 12/17?
SQL: SELECT Item FROM Items JOIN Orders ON Items.Id = Orders.Item_Id JOIN Consumers ON Consumers.Id = Orders.Consumer_Id WHERE Consumers.Name = 'Lily' and Orders.Date = '12/17' 

Q: How much did Amy spend on 12/19?
SQL: SELECT SUM(Total_Amount) FROM Orders JOIN Consumers ON Orders.Consumer_Id = Consumers.Id WHERE Consumers.Name = 'Amy' AND Date = '12/19'

"""

sql_norm_del_value_rule = """
# Through the database regularization process, learn how to write SQL query
The normal forms (from least normalized to most normalized) are: UNF(Unnormalized form), 1NF(First normal form), 2NF(Second normal form), 3NF(Third normal form).
Now, we have an initial data(UNF data):
Table Comsumptions, columns = [*,Name,Sex,Gender,Item,Price,Quantity,Store,Date,Order_Number]
## Text-to-SQL example:
Q: What did Lily buy on 12/17?
SQL: SELECT Item FROM Comsumptions WHERE Name = 'Lily' and Date = '12/17' 

In the initial table, Item and Quantity contain multiple values. Sex and Gender have the same meaning. In the table, there is no primary key.
## Based on 1NF, the new table:
Table Comsumptions, columns = [*,Name,Sex,Item,Price,Quantity,Total_Amount,Store,Date,Order_Number]
Table Comsumptions, primary_keys = [Name,Item,Quantity,Store,Date,Order_Number]
# Text-to-SQL example:
Q: What did Lily buy on 12/17?
SQL: SELECT Item FROM Comsumptions WHERE Name = 'Lily' and Date = '12/17' 

Q: How much did Amy spend on 12/19?
SQL: SELECT SUM(*) FROM Comsumptions WHERE Name='Amy' and Date = '12/19'

In the 1NF table, every consumption record records the gender of the consumer, the name of the store, and there are too many duplicates.
## Based on 2NF, the new table:
Table Consumers, columns = [*,Id,Name,Sex]
Table Consumers, primary_keys = [Id]
Table Shops, columns = [*,Id,Store]
Table Shops, primary_keys = [Id]
Table Items, columns = [*,Id,Item,Price,Store_Id]
Table Items, primary_keys = [Id]
Table Orders, columns = [*,Id,Consumer_Id,Item_Id,Quantity,Total_Amount,Date,Order_Number]
Table Orders, primary_keys = [Id]
## Text-to-SQL example:
Q: What did Lily buy on 12/17?
SQL: SELECT Item FROM Items JOIN Orders ON Items.Id = Orders.Item_Id JOIN Consumers ON Consumers.Id = Orders.Consumer_Id WHERE Consumers.Name = 'Lily' and Orders.Date = '12/17' 

Q: How much did Amy spend on 12/19?
SQL: SELECT SUM(Total_Amount) FROM Orders JOIN Consumers ON Orders.Consumer_Id = Consumers.Id WHERE Consumers.Name = 'Amy' AND Date = '12/19'

"""

reverse_sql_norm = """
# Use a database to realize how to join multiple tables.
If table schema is like this:
Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]
Foreign_keys = [department.Department_ID = management.department_ID,head.head_ID = management.head_ID]
Q: Show the name and number of employees for the departments managed by heads whose temporary acting value is 'Yes'?
A: Let's think step by step. In the question, we have to know the name and number of employees, so we need department table. we have to know whose temporary acting value is 'Yes', so we need management table. So, we need to join these tables = [department,management]. When we join these table, we need to use foreign key to connect them.
SQL: SELECT T1.name ,  T1.num_employees FROM department AS T1 JOIN management AS T2 ON T1.department_id  =  T2.department_id WHERE T2.temporary_acting  =  'Yes'

Second, if table schema is like this:
Table department_management, column = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees,head_ID,temporary_acting]
Q: Show the name and number of employees for the departments managed by heads whose temporary acting value is 'Yes'?
A: Let's think step by step. the name and number of employees and temporary acting value are in department_management table.
SQL: SELECT name, num_employees FROM department_management WHERE temporary_acting  =  'Yes'
"""


"""
Q: How much milk was sold on 12/19?
SQL:
"""

set_param = """
please follow the param:
    model = "3.5",
    n = 1,
    stream = False,
    temperature=0.0,
    max_tokens=600,
    top_p = 1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop = ["Q:"]

"""


"""

In the question "How many singers do we have?", we are asked:
"How many singers" so we need column = [COUNT(singer.Singer_ID)]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = []. So the Schema_links are:
Schema_links: [COUNT(singer.Singer_ID)]

"""

"""
SELECT T1.name ,  T1.num_employees 
FROM department AS T1 JOIN management AS T2 ON T1.department_id  =  T2.department_id 
WHERE T2.temporary_acting  =  'Yes'
"""