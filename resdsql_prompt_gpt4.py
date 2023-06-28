# ----------------------------------------------------prompts-----------------------------------------------
schema_linking_prompt = """Table advisor, columns = [*,s_ID,i_ID]
Table classroom, columns = [*,building,room_number,capacity]
Table course, columns = [*,course_id,title,dept_name,credits]
Table department, columns = [*,dept_name,building,budget]
Table instructor, columns = [*,ID,name,dept_name,salary]
Table prereq, columns = [*,course_id,prereq_id]
Table section, columns = [*,course_id,sec_id,semester,year,building,room_number,time_slot_id]
Table student, columns = [*,ID,name,dept_name,tot_cred]
Table takes, columns = [*,ID,course_id,sec_id,semester,year,grade]
Table teaches, columns = [*,ID,course_id,sec_id,semester,year]
Table time_slot, columns = [*,time_slot_id,day,start_hr,start_min,end_hr,end_min]
Foreign_keys = [course.dept_name = department.dept_name,instructor.dept_name = department.dept_name,section.building = classroom.building,section.room_number = classroom.room_number,section.course_id = course.course_id,teaches.ID = instructor.ID,teaches.course_id = section.course_id,teaches.sec_id = section.sec_id,teaches.semester = section.semester,teaches.year = section.year,student.dept_name = department.dept_name,takes.ID = student.ID,takes.course_id = section.course_id,takes.sec_id = section.sec_id,takes.semester = section.semester,takes.year = section.year,advisor.s_ID = student.ID,advisor.i_ID = instructor.ID,prereq.prereq_id = course.course_id,prereq.course_id = course.course_id]
Q: "Find the buildings which have rooms with capacity more than 50."
A: Let’s think step by step. In the question "Find the buildings which have rooms with capacity more than 50.", we are asked:
"the buildings which have rooms" so we need column = [classroom.capacity]
"rooms with capacity" so we need column = [classroom.building]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [50]. So the Schema_links are:
Schema_links: [classroom.building,classroom.capacity,50]

Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]
Foreign_keys = [management.head_ID = head.head_ID,management.department_ID = department.Department_ID]
Q: "How many heads of the departments are older than 56 ?"
A: Let’s think step by step. In the question "How many heads of the departments are older than 56 ?", we are asked:
"How many heads of the departments" so we need column = [head.*]
"older" so we need column = [head.age]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [56]. So the Schema_links are:
Schema_links: [head.*,head.age,56]

Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]
Foreign_keys = [management.head_ID = head.head_ID,management.department_ID = department.Department_ID]
Q: "what are the distinct creation years of the departments managed by a secretary born in state 'Alabama'?"
A: Let’s think step by step. In the question "what are the distinct creation years of the departments managed by a secretary born in state 'Alabama'?", we are asked:
"distinct creation years of the departments" so we need column = [department.Creation]
"departments managed by" so we need column = [management.department_ID]
"born in" so we need column = [head.born_state]
Based on the columns and tables, we need these Foreign_keys = [department.Department_ID = management.department_ID,management.head_ID = head.head_ID].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = ['Alabama']. So the Schema_links are:
Schema_links: [department.Creation,department.Department_ID = management.department_ID,head.head_ID = management.head_ID,head.born_state,'Alabama']

Table Addresses, columns = [*,address_id,line_1,line_2,city,zip_postcode,state_province_county,country]
Table Candidate_Assessments, columns = [*,candidate_id,qualification,assessment_date,asessment_outcome_code]
Table Candidates, columns = [*,candidate_id,candidate_details]
Table Courses, columns = [*,course_id,course_name,course_description,other_details]
Table People, columns = [*,person_id,first_name,middle_name,last_name,cell_mobile_number,email_address,login_name,password]
Table People_Addresses, columns = [*,person_address_id,person_id,address_id,date_from,date_to]
Table Student_Course_Attendance, columns = [*,student_id,course_id,date_of_attendance]
Table Student_Course_Registrations, columns = [*,student_id,course_id,registration_date]
Table Students, columns = [*,student_id,student_details]
Foreign_keys = [Students.student_id = People.person_id,People_Addresses.address_id = Addresses.address_id,People_Addresses.person_id = People.person_id,Student_Course_Registrations.course_id = Courses.course_id,Student_Course_Registrations.student_id = Students.student_id,Student_Course_Attendance.student_id = Student_Course_Registrations.student_id,Student_Course_Attendance.course_id = Student_Course_Registrations.course_id,Candidates.candidate_id = People.person_id,Candidate_Assessments.candidate_id = Candidates.candidate_id]
Q: "List the id of students who never attends courses?"
A: Let’s think step by step. In the question "List the id of students who never attends courses?", we are asked:
"id of students" so we need column = [Students.student_id]
"never attends courses" so we need column = [Student_Course_Attendance.student_id]
Based on the columns and tables, we need these Foreign_keys = [Students.student_id = Student_Course_Attendance.student_id].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = []. So the Schema_links are:
Schema_links: [Students.student_id = Student_Course_Attendance.student_id]

Table Country, columns = [*,id,name]
Table League, columns = [*,id,country_id,name]
Table Player, columns = [*,id,player_api_id,player_name,player_fifa_api_id,birthday,height,weight]
Table Player_Attributes, columns = [*,id,player_fifa_api_id,player_api_id,date,overall_rating,potential,preferred_foot,attacking_work_rate,defensive_work_rate,crossing,finishing,heading_accuracy,short_passing,volleys,dribbling,curve,free_kick_accuracy,long_passing,ball_control,acceleration,srecord.write_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,aggression,interceptions,positioning,vision,penalties,marking,standing_tackle,sliding_tackle,gk_diving,gk_handling,gk_kicking,gk_positioning,gk_reflexes]
Table Team, columns = [*,id,team_api_id,team_fifa_api_id,team_long_name,team_short_name]
Table Team_Attributes, columns = [*,id,team_fifa_api_id,team_api_id,date,buildUpPlaySpeed,buildUpPlaySpeedClass,buildUpPlayDribbling,buildUpPlayDribblingClass,buildUpPlayPassing,buildUpPlayPassingClass,buildUpPlayPositioningClass,chanceCreationPassing,chanceCreationPassingClass,chanceCreationCrossing,chanceCreationCrossingClass,chanceCreationShooting,chanceCreationShootingClass,chanceCreationPositioningClass,defencePressure,defencePressureClass,defenceAggression,defenceAggressionClass,defenceTeamWidth,defenceTeamWidthClass,defenceDefenderLineClass]
Table sqlite_sequence, columns = [*,name,seq]
Foreign_keys = [Player_Attributes.player_api_id = Player.player_api_id,Player_Attributes.player_fifa_api_id = Player.player_fifa_api_id,League.country_id = Country.id,Team_Attributes.team_api_id = Team.team_api_id,Team_Attributes.team_fifa_api_id = Team.team_fifa_api_id]
Q: "List the names of all left-footed players who have overall rating between 85 and 90."
A: Let’s think step by step. In the question "List the names of all left-footed players who have overall rating between 85 and 90.", we are asked:
"names of all left-footed players" so we need column = [Player.player_name,Player_Attributes.preferred_foot]
"players who have overall rating" so we need column = [Player_Attributes.overall_rating]
Based on the columns and tables, we need these Foreign_keys = [Player_Attributes.player_api_id = Player.player_api_id].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [left,85,90]. So the Schema_links are:
Schema_links: [Player.player_name,Player_Attributes.preferred_foot,Player_Attributes.overall_rating,Player_Attributes.player_api_id = Player.player_api_id,left,85,90]

Table advisor, columns = [*,s_ID,i_ID]
Table classroom, columns = [*,building,room_number,capacity]
Table course, columns = [*,course_id,title,dept_name,credits]
Table department, columns = [*,dept_name,building,budget]
Table instructor, columns = [*,ID,name,dept_name,salary]
Table prereq, columns = [*,course_id,prereq_id]
Table section, columns = [*,course_id,sec_id,semester,year,building,room_number,time_slot_id]
Table student, columns = [*,ID,name,dept_name,tot_cred]
Table takes, columns = [*,ID,course_id,sec_id,semester,year,grade]
Table teaches, columns = [*,ID,course_id,sec_id,semester,year]
Table time_slot, columns = [*,time_slot_id,day,start_hr,start_min,end_hr,end_min]
Foreign_keys = [course.dept_name = department.dept_name,instructor.dept_name = department.dept_name,section.building = classroom.building,section.room_number = classroom.room_number,section.course_id = course.course_id,teaches.ID = instructor.ID,teaches.course_id = section.course_id,teaches.sec_id = section.sec_id,teaches.semester = section.semester,teaches.year = section.year,student.dept_name = department.dept_name,takes.ID = student.ID,takes.course_id = section.course_id,takes.sec_id = section.sec_id,takes.semester = section.semester,takes.year = section.year,advisor.s_ID = student.ID,advisor.i_ID = instructor.ID,prereq.prereq_id = course.course_id,prereq.course_id = course.course_id]
Q: "Give the title of the course offered in Chandler during the Fall of 2010."
A: Let’s think step by step. In the question "Give the title of the course offered in Chandler during the Fall of 2010.", we are asked:
"title of the course" so we need column = [course.title]
"course offered in Chandler" so we need column = [SECTION.building]
"during the Fall" so we need column = [SECTION.semester]
"of 2010" so we need column = [SECTION.year]
Based on the columns and tables, we need these Foreign_keys = [course.course_id = SECTION.course_id].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [Chandler,Fall,2010]. So the Schema_links are:
Schema_links: [course.title,course.course_id = SECTION.course_id,SECTION.building,SECTION.year,SECTION.semester,Chandler,Fall,2010]

Table city, columns = [*,City_ID,Official_Name,Status,Area_km_2,Population,Census_Ranking]
Table competition_record, columns = [*,Competition_ID,Farm_ID,Rank]
Table farm, columns = [*,Farm_ID,Year,Total_Horses,Working_Horses,Total_Cattle,Oxen,Bulls,Cows,Pigs,Sheep_and_Goats]
Table farm_competition, columns = [*,Competition_ID,Year,Theme,Host_city_ID,Hosts]
Foreign_keys = [farm_competition.Host_city_ID = city.City_ID,competition_record.Farm_ID = farm.Farm_ID,competition_record.Competition_ID = farm_competition.Competition_ID]
Q: "Show the status of the city that has hosted the greatest number of competitions."
A: Let’s think step by step. In the question "Show the status of the city that has hosted the greatest number of competitions.", we are asked:
"the status of the city" so we need column = [city.Status]
"greatest number of competitions" so we need column = [farm_competition.*]
Based on the columns and tables, we need these Foreign_keys = [farm_competition.Host_city_ID = city.City_ID].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = []. So the Schema_links are:
Schema_links: [city.Status,farm_competition.Host_city_ID = city.City_ID,farm_competition.*]

Table advisor, columns = [*,s_ID,i_ID]
Table classroom, columns = [*,building,room_number,capacity]
Table course, columns = [*,course_id,title,dept_name,credits]
Table department, columns = [*,dept_name,building,budget]
Table instructor, columns = [*,ID,name,dept_name,salary]
Table prereq, columns = [*,course_id,prereq_id]
Table section, columns = [*,course_id,sec_id,semester,year,building,room_number,time_slot_id]
Table student, columns = [*,ID,name,dept_name,tot_cred]
Table takes, columns = [*,ID,course_id,sec_id,semester,year,grade]
Table teaches, columns = [*,ID,course_id,sec_id,semester,year]
Table time_slot, columns = [*,time_slot_id,day,start_hr,start_min,end_hr,end_min]
Foreign_keys = [course.dept_name = department.dept_name,instructor.dept_name = department.dept_name,section.building = classroom.building,section.room_number = classroom.room_number,section.course_id = course.course_id,teaches.ID = instructor.ID,teaches.course_id = section.course_id,teaches.sec_id = section.sec_id,teaches.semester = section.semester,teaches.year = section.year,student.dept_name = department.dept_name,takes.ID = student.ID,takes.course_id = section.course_id,takes.sec_id = section.sec_id,takes.semester = section.semester,takes.year = section.year,advisor.s_ID = student.ID,advisor.i_ID = instructor.ID,prereq.prereq_id = course.course_id,prereq.course_id = course.course_id]
Q: "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010."
A: Let’s think step by step. In the question "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010.", we are asked:
"id of instructors who taught " so we need column = [teaches.id]
"taught a class in" so we need column = [teaches.semester,teaches.year]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [Fall,2009,Spring,2010]. So the Schema_links are:
schema_links: [teaches.id,teaches.semester,teaches.year,Fall,2009,Spring,2010]

Table Accounts, columns = [*,account_id,customer_id,date_account_opened,account_name,other_account_details]
Table Customers, columns = [*,customer_id,customer_first_name,customer_middle_initial,customer_last_name,gender,email_address,login_name,login_password,phone_number,town_city,state_county_province,country]
Table Financial_Transactions, columns = [*,transaction_id,account_id,invoice_number,transaction_type,transaction_date,transaction_amount,transaction_comment,other_transaction_details]
Table Invoice_Line_Items, columns = [*,order_item_id,invoice_number,product_id,product_title,product_quantity,product_price,derived_product_cost,derived_vat_payable,derived_total_cost]
Table Invoices, columns = [*,invoice_number,order_id,invoice_date]
Table Order_Items, columns = [*,order_item_id,order_id,product_id,product_quantity,other_order_item_details]
Table Orders, columns = [*,order_id,customer_id,date_order_placed,order_details]
Table Product_Categories, columns = [*,production_type_code,product_type_description,vat_rating]
Table Products, columns = [*,product_id,parent_product_id,production_type_code,unit_price,product_name,product_color,product_size]
Foreign_keys = [Orders.customer_id = Customers.customer_id,Invoices.order_id = Orders.order_id,Accounts.customer_id = Customers.customer_id,Products.production_type_code = Product_Categories.production_type_code,Financial_Transactions.account_id = Accounts.account_id,Financial_Transactions.invoice_number = Invoices.invoice_number,Order_Items.order_id = Orders.order_id,Order_Items.product_id = Products.product_id,Invoice_Line_Items.product_id = Products.product_id,Invoice_Line_Items.invoice_number = Invoices.invoice_number,Invoice_Line_Items.order_item_id = Order_Items.order_item_id]
Q: "Show the id, the date of account opened, the account name, and other account detail for all accounts."
A: Let’s think step by step. In the question "Show the id, the date of account opened, the account name, and other account detail for all accounts.", we are asked:
"the id, the date of account opened, the account name, and other account detail for all accounts." so we need column = [Accounts.account_id,Accounts.account_name,Accounts.other_account_details,Accounts.date_account_opened]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = []. So the Schema_links are:
Schema_links: [Accounts.account_id,Accounts.account_name,Accounts.other_account_details,Accounts.date_account_opened]

Table city, columns = [*,City_ID,Official_Name,Status,Area_km_2,Population,Census_Ranking]
Table competition_record, columns = [*,Competition_ID,Farm_ID,Rank]
Table farm, columns = [*,Farm_ID,Year,Total_Horses,Working_Horses,Total_Cattle,Oxen,Bulls,Cows,Pigs,Sheep_and_Goats]
Table farm_competition, columns = [*,Competition_ID,Year,Theme,Host_city_ID,Hosts]
Foreign_keys = [farm_competition.Host_city_ID = city.City_ID,competition_record.Farm_ID = farm.Farm_ID,competition_record.Competition_ID = farm_competition.Competition_ID]
Q: "Show the status shared by cities with population bigger than 1500 and smaller than 500."
A: Let’s think step by step. In the question "Show the status shared by cities with population bigger than 1500 and smaller than 500.", we are asked:
"the status shared by cities" so we need column = [city.Status]
"cities with population" so we need column = [city.Population]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [1500,500]. So the Schema_links are:
Schema_links: [city.Status,city.Population,1500,500]

"""
classification_prompt = """Q: "Find the buildings which have rooms with capacity more than 50."
schema_links: [classroom.building,classroom.capacity,50]
A: Let’s think step by step. The SQL query for the question "Find the buildings which have rooms with capacity more than 50." needs these tables = [classroom], so we don't need JOIN.
Plus, it doesn't require nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN), and we need the answer to the questions = [""].
So, we don't need JOIN and don't need nested queries, then the the SQL query can be classified as "EASY".
Label: "EASY"

Q: "What are the names of all instructors who advise students in the math depart sorted by total credits of the student."
schema_links: [advisor.i_id = instructor.id,advisor.s_id = student.id,instructor.name,student.dept_name,student.tot_cred,math]
A: Let’s think step by step. The SQL query for the question "What are the names of all instructors who advise students in the math depart sorted by total credits of the student." needs these tables = [advisor,instructor,student], so we need JOIN.
Plus, it doesn't need nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN), and we need the answer to the questions = [""].
So, we need JOIN and don't need nested queries, then the the SQL query can be classified as "NON-NESTED".
Label: "NON-NESTED"

Q: "Find the room number of the rooms which can sit 50 to 100 students and their buildings."
schema_links: [classroom.building,classroom.room_number,classroom.capacity,50,100]
A: Let’s think step by step. The SQL query for the question "Find the room number of the rooms which can sit 50 to 100 students and their buildings." needs these tables = [classroom], so we don't need JOIN.
Plus, it doesn't require nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN), and we need the answer to the questions = [""].
So, we don't need JOIN and don't need nested queries, then the the SQL query can be classified as "EASY".
Label: "EASY"

Q: "How many courses that do not have prerequisite?"
schema_links: [course.*,course.course_id = prereq.course_id]
A: Let’s think step by step. The SQL query for the question "How many courses that do not have prerequisite?" needs these tables = [course,prereq], so we need JOIN.
Plus, it requires nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN), and we need the answer to the questions = ["Which courses have prerequisite?"].
So, we need JOIN and need nested queries, then the the SQL query can be classified as "NESTED".
Label: "NESTED"

Q: "Find the title of course that is provided by both Statistics and Psychology departments."
schema_links: [course.title,course.dept_name,Statistics,Psychology]
A: Let’s think step by step. The SQL query for the question "Find the title of course that is provided by both Statistics and Psychology departments." needs these tables = [course], so we don't need JOIN.
Plus, it requires nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN), and we need the answer to the questions = ["Find the titles of courses that is provided by Psychology departments"].
So, we don't need JOIN and need nested queries, then the the SQL query can be classified as "NESTED".
Label: "NESTED"

Q: "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010."
schema_links: [teaches.id,teaches.semester,teaches.year,Fall,2009,Spring,2010]
A: Let’s think step by step. The SQL query for the question "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010." needs these tables = [teaches], so we don't need JOIN.
Plus, it requires nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN), and we need the answer to the questions = ["Find the id of instructors who taught a class in Spring 2010"].
So, we don't need JOIN and need nested queries, then the the SQL query can be classified as "NESTED".
Label: "NESTED"

Q: "Find the name of the department that offers the highest total credits?"
schema_links: [course.dept_name,course.credits]
A: Let’s think step by step. The SQL query for the question "Find the name of the department that offers the highest total credits?." needs these tables = [course], so we don't need JOIN.
Plus, it doesn't require nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN), and we need the answer to the questions = [""].
So, we don't need JOIN and don't need nested queries, then the the SQL query can be classified as "EASY".
Label: "EASY"

Q: "What is the name of the instructor who advises the student with the greatest number of total credits?"
schema_links: [advisor.i_id = instructor.id,advisor.s_id = student.id,instructor.name,student.tot_cred ]
A: Let’s think step by step. The SQL query for the question "What is the name of the instructor who advises the student with the greatest number of total credits?" needs these tables = [advisor,instructor,student], so we need JOIN.
Plus, it doesn't need nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN), and we need the answer to the questions = [""].
So, we need JOIN and don't need nested queries, then the the SQL query can be classified as "NON-NESTED".
Label: "NON-NESTED"

Q: "Find the total number of students and total number of instructors for each department."
schema_links = [department.dept_name = instructor.dept_name,student.id,student.dept_name = department.dept_name,instructor.id]
A: Let’s think step by step. The SQL query for the question "Find the total number of students and total number of instructors for each department." needs these tables = [department,instructor,student], so we need JOIN.
Plus, it doesn't need nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN), and we need the answer to the questions = [""].
So, we need JOIN and don't need nested queries, then the the SQL query can be classified as "NON-NESTED".
Label: "NON-NESTED"

Q: "Give the name and building of the departments with greater than average budget."
schema_links: [department.budget,department.dept_name,department.building]
A: Let’s think step by step. The SQL query for the question "Give the name and building of the departments with greater than average budget." needs these tables = [department], so we don't need JOIN.
Plus, it requires nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN), and we need the answer to the questions = ["What is the average budget of the departments"].
So, we don't need JOIN and need nested queries, then the the SQL query can be classified as "NESTED".
Label: "NESTED"

"""

get_n_of_tables_prompt = """Q: "Find the buildings which have rooms with capacity more than 50."
schema_links: [classroom.building,classroom.capacity,50]
A: Let’s think step by step. The question is "Find the buildings which have [rooms] with capacity more than 50.". [rooms] matches table = [classroom]. So, tables = [classroom]. If number of tables = 1, predict EASY or NESTED.
Plus, from question, no sentence matches nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN). If nested queries don't exist, predict EASY or NON-NESTED.
So, first step, classification is EASY or NESTED, and second step, classification is EASY or NON-NESTED. Finally, the SQL query can be classified as "EASY".
Label: "EASY"

Q: "What are the names of all instructors who advise students in the math depart sorted by total credits of the student."
schema_links: [advisor.i_id = instructor.id,advisor.s_id = student.id,instructor.name,student.dept_name,student.tot_cred,math]
A: Let’s think step by step. The question is "What are the names of all [instructors] who advise [students] in the math depart sorted by total credits of the student.". [instructors] matches table = [instructor]. [students] matches table = [student]. tables = [instructor, student] are connected by table = [advisor]. So, tables = [instructor, student, advisor]. If number of tables >= 1, predict NON-NESTED or NESTED.
Plus, from question, no sentence matches nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN). If nested queries don't exist, predict EASY or NON-NESTED.
So, first step, classification is NON-NESTED or NESTED, and second step, classification is EASY or NON-NESTED. Finally, the SQL query can be classified as "NON-NESTED".
Label: "NON-NESTED"

Q: "Find the room number of the rooms which can sit 50 to 100 students and their buildings."
schema_links: [classroom.building,classroom.room_number,classroom.capacity,50,100]
A: Let’s think step by step. The question is "Find the room number of the [rooms] which can sit 50 to 100 students and their buildings." [rooms] matches table = [classroom]. So, tables = [classroom]. If number of tables = 1, predict EASY or NESTED.
Plus, from question, no sentence matches nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN). If nested queries don't exist, predict EASY or NON-NESTED.
So, first step, classification is EASY or NESTED, and second step, classification is EASY or NON-NESTED. Finally, the SQL query can be classified as "EASY".
Label: "EASY"

Q: "How many courses that do not have prerequisite?"
schema_links: [course.*,course.course_id = prereq.course_id]
A: Let’s think step by step. The question is "How many [courses] that do not have [prerequisite]?". [courses] matches table = [course]. [prerequisite] matches table = [prereq]. So, tables = [course, prereq]. If number of tables >= 1, predict NON-NESTED or NESTED.
Plus, from question, "Which courses have prerequisite?" matches nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN). If nested queries exist, predict NESTED.
So, first step, classification is NON-NESTED or NESTED, and second step, classification is NESTED. Finally, the SQL query can be classified as "NESTED".
Label: "NESTED"

Q: "Find the title of course that is provided by both Statistics and Psychology departments."
schema_links: [course.title,course.dept_name,Statistics,Psychology]
A: Let’s think step by step. The question is "Find the title of [course] that is provided by both Statistics and Psychology departments.". [course] matches table = [course]. So, tables = [course]. If number of tables = 1, predict EASY or NESTED.
Plus, from question, "Find the titles of courses that is provided by Psychology departments" matches nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN). If nested queries exist, predict NESTED.
So, first step, classification is EASY or NESTED, and second step, classification is NESTED. Finally, the SQL query can be classified as "NESTED".
Label: "NESTED"

Q: "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010."
schema_links: [teaches.id,teaches.semester,teaches.year,Fall,2009,Spring,2010]
A: Let’s think step by step. The question is "Find the id of instructors who [taught] a class in Fall 2009 but not in Spring 2010.". [taught] matches table = [teaches]. So, tables = [teaches]. If number of tables = 1, predict EASY or NESTED.
Plus, from question, "Find the id of instructors who taught a class in Spring 2010" matches nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN). If nested queries exist, predict NESTED.
So, first step, classification is EASY or NESTED, and second step, classification is NESTED. Finally, the SQL query can be classified as "NESTED".
Label: "NESTED"

Q: "Find the name of the department that offers the highest total credits?"
schema_links: [course.dept_name,course.credits]
A: Let’s think step by step. The question is "Find the name of the [department] that offers the highest total [credits]?." [department, credits] matches tables = [course]. So, tables = [course]. If number of tables = 1, predict EASY or NESTED.
Plus, from question, no sentence matches nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN). If nested queries don't exist, predict EASY or NON-NESTED.
So, first step, classification is EASY or NESTED, and second step, classification is EASY or NON-NESTED. Finally, the SQL query can be classified as "EASY".
Label: "EASY"

Q: "What is the name of the instructor who advises the student with the greatest number of total credits?"
schema_links: [advisor.i_id = instructor.id,advisor.s_id = student.id,instructor.name,student.tot_cred ]
A: Let’s think step by step. The question is "What is the name of the [instructor] who advises the [student] with the greatest number of total credits?". [instructors] matches table = [instructor]. [students] matches table = [student]. tables = [instructor, student] are connected by table = [advisor]. So, tables = [instructor, student, advisor]. If number of tables >= 1, predict NON-NESTED or NESTED.
Plus, from question, no sentence matches nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN). If nested queries don't exist, predict EASY or NON-NESTED.
So, first step, classification is NON-NESTED or NESTED, and second step, classification is EASY or NON-NESTED. Finally, the SQL query can be classified as "NON-NESTED".
Label: "NON-NESTED"

Q: "Find the total number of students and total number of instructors for each department."
schema_links = [department.dept_name = instructor.dept_name,student.id,student.dept_name = department.dept_name,instructor.id]
A: Let’s think step by step. The question is "Find the total number of [students] and total number of [instructors] for each [department].". [students] matches table = [student]. [instructors] matches [instructor]. [department] matches [department]. So, tables = [student, instructor, department]. If number of tables >= 1, predict NON-NESTED or NESTED.
Plus, from question, no sentence matches nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN). If nested queries don't exist, predict EASY or NON-NESTED.
So, first step, classification is NON-NESTED or NESTED, and second step, classification is EASY or NON-NESTED. Finally, the SQL query can be classified as "NON-NESTED".
Label: "NON-NESTED"

Q: "Give the name and building of the departments with greater than average budget."
schema_links: [department.budget,department.dept_name,department.building]
A: Let’s think step by step. The question is "Give the name and building of the [departments] with greater than average budget.". [departments] matches table = [department]. So, tables = [department]. If number of tables = 1, predict EASY or NESTED.
Plus, from question, "What is the average budget of the departments" matchesS nested queries with (INTERSECT, UNION, EXCEPT, IN, NOT IN). If nested queries exist, predict NESTED.
So, first step, classification is EASY or NESTED, and second step, classification is NESTED. Finally, the SQL query can be classified as "NESTED".
Label: "NESTED"

"""

resd_prompt = """
input = Find the buildings which have rooms with capacity more than 50. | classroom : classroom.building , classroom.capacity , classroom.room_number , classroom.* | department : department.budget , department.building , department.dept_name , department.* | student : student.dept_name , student.id , student.tot_cred , student.name , student.* | advisor : advisor.s_id , advisor.i_id , advisor.*
natsql = select distinct _ from _ where _ | select distinct classroom.building from classroom where classroom.capacity > 50
SQL = SELECT DISTINCT building FROM classroom WHERE capacity  >  50

input = What is the name of the department with the most credits? | course : course.dept_name , course.credits , course.title , course.course_id , course.* | prereq : prereq.prereq_id , prereq.course_id , prereq.* | section : section.sec_id , section.year , section.room_number , section.course_id , section.time_slot_id , section.* | takes : takes.semester , takes.id , takes.grade , takes.year , takes.course_id , takes.*
natsql = select _ from _ group by _ order by sum ( _ ) desc limit _  | select course.dept_name from course group by course.dept_name order by sum ( course.credits ) desc limit 1
SQL = SELECT dept_name FROM course GROUP BY dept_name ORDER BY sum(credits) DESC LIMIT 1

input = What are the names and average salaries for departments with average salary higher than 42000? | instructor : instructor.name , instructor.dept_name , instructor.id , instructor.salary , instructor.* | teaches : teaches.course_id , teaches.sec_id , teaches.id , teaches.semester , teaches.year , teaches.* | time_slot : time_slot.end_min , time_slot.end_hr , time_slot.start_hr , time_slot.day , time_slot.start_min , time_slot.* | prereq : prereq.course_id , prereq.prereq_id , prereq.*"
natsql = select _ , avg ( _ ) from _ where avg ( _ ) > _ group by _ | select instructor.dept_name , avg ( instructor.salary ) from instructor where avg ( instructor.salary ) > 42000 group by instructor.dept_name
SQL = SELECT dept_name ,  AVG (salary) FROM instructor GROUP BY dept_name HAVING AVG (salary)  >  42000

input = What is the name and building of the departments whose budget is more than the average budget? | department : department.dept_name , department.budget , department.building , department.* | takes : takes.sec_id , takes.year , takes.grade , takes.id , takes.course_id , takes.* | time_slot : time_slot.day , time_slot.time_slot_id , time_slot.start_min , time_slot.start_hr , time_slot.end_min , time_slot.* | instructor : instructor.name , instructor.dept_name , instructor.salary , instructor.id , instructor.*
natsql = select _ from _ where @.@ > avg ( _ ) | select department.dept_name , department.building from department where @.@ > avg ( department.budget )
SQL = SELECT dept_name ,  building FROM department WHERE budget  >  (SELECT avg(budget) FROM department)

input = Find the total number of students and total number of instructors for each department. | department : department.dept_name , department.budget , department.building , department.* | instructor : instructor.name , instructor.salary , instructor.id , instructor.dept_name , instructor.* | student : student.id , student.name , student.dept_name , student.tot_cred , student.* | takes : takes.year , takes.semester , takes.grade , takes.course_id , takes.sec_id , takes.*
natsql = select count ( distinct _ ) , count ( distinct _ ) , _ from _ group by _ | select count ( distinct student.id ) , count ( distinct instructor.id ) , department.dept_name from department group by instructor.dept_name
SQL = SELECT count(DISTINCT T2.id) ,  count(DISTINCT T3.id) ,  T3.dept_name FROM department AS T1 JOIN student AS T2 ON T1.dept_name  =  T2.dept_name JOIN instructor AS T3 ON T1.dept_name  =  T3.dept_name GROUP BY T3.dept_name

input = Find the name of students who took any class in the years of 2009 and 2010. | student : student.name , student.tot_cred , student.id , student.dept_name , student.* | takes : takes.year , takes.sec_id , takes.grade , takes.semester , takes.id , takes.* | time_slot : time_slot.end_hr , time_slot.day , time_slot.start_hr , time_slot.start_min , time_slot.end_min , time_slot.* | section : section.year , section.sec_id , section.time_slot_id , section.room_number , section.course_id , section.*
natsql = select distinct _ from _ where _  | select distinct student.name from student where takes.year = 2009 or takes.year = 2010
SQL = SELECT DISTINCT T1.name FROM student AS T1 JOIN takes AS T2 ON T1.id  =  T2.id WHERE YEAR  =  2009 OR YEAR  =  2010

input = Find the name and building of the department with the highest budget. | department : department.dept_name , department.building , department.budget , department.* | time_slot : time_slot.time_slot_id , time_slot.day , time_slot.end_min , time_slot.start_hr , time_slot.end_hr , time_slot.* | takes : takes.year , takes.grade , takes.id , takes.semester , takes.sec_id , takes.* | classroom : classroom.room_number , classroom.capacity , classroom.building , classroom.*
natsql = select _ from _ order by _ desc limit _ | select department.dept_name , department.building from department order by department.budget desc limit 1
SQL = SELECT dept_name ,  building FROM department ORDER BY budget DESC LIMIT 1

input = Give the title and credits for the course that is taught in the classroom with the greatest capacity. | classroom : classroom.capacity , classroom.building , classroom.room_number , classroom.* | course : course.dept_name , course.title , course.credits , course.course_id , course.* | department : department.dept_name , department.building , department.budget , department.* | advisor : advisor.s_id , advisor.i_id , advisor.*
natsql = select _ from _ where @.@ = max ( _ ) | select course.title , course.credits from classroom where @.@ = max ( classroom.capacity )
SQL = SELECT T3.title ,  T3.credits FROM classroom AS T1 JOIN SECTION AS T2 ON T1.building  =  T2.building AND T1.room_number  =  T2.room_number JOIN course AS T3 ON T2.course_id  =  T3.course_id WHERE T1.capacity  =  (SELECT max(capacity) FROM classroom)

input = Find the title of the course that is offered by more than one department. | course : course.title , course.credits , course.dept_name , course.course_id , course.* | takes : takes.semester , takes.course_id , takes.sec_id , takes.year , takes.grade , takes.* | section : section.course_id , section.sec_id , section.time_slot_id , section.semester , section.year , section.* | teaches : teaches.semester , teaches.year , teaches.id , teaches.sec_id , teaches.course_id , teaches.*
natsql = select _ from _ where count ( _ ) > _ group by _ | select course.title from course where count ( course.* ) > 1 group by course.title
SQL = SELECT title FROM course GROUP BY title HAVING count(*)  >  1
"""

# ----------------------------------------------------------------------------------------------------------

from revChatGPT.V1 import Chatbot
import json

f = open('config.json')
config = json.load(f)
config['model'] = "gpt-4"

import pandas as pd
import time
import os
import sys
import random

tmp_config = {"dateset": "./data/", "output": "predicted_sql.txt"}
# if sys.argv[1] == "--dataset" and sys.argv[3] == "--output":
DATASET_SCHEMA = tmp_config["dateset"] + "tables.json"
DATASET = tmp_config["dateset"] + "dev.json"
OUTPUT_FILE = tmp_config["output"]
FILE_PATH = "my_result/resqsql"
SCHEMA_LINK_PATH = f"{FILE_PATH}/schema_link.txt"

def load_schema_link_list(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f]


def get_pay_chatbot(index):
    # print('pay index: ', index)
    pay_count = 4
    name = "access_token_charlie"
    if index % pay_count == 0:
        name = "access_token_3744"
    elif index % pay_count == 1:
        name = "access_token_vic"
    elif index % pay_count == 2:
        name = "access_token_lab"
    elif index % pay_count == 3:
        pass
    #     rand_int = random.randrange(5)
    #     # 為了讓這隻帳號不要被跑太多次
    #     if rand_int == 0:
    #         name = "access_token_3744"
    #     elif rand_int == 1:
    #         name = "access_token_vic"
    #     elif rand_int == 2:
    #         name = "access_token_lab"
    #     elif rand_int == 3:
    #         name = "access_token_charlie"
    #     elif rand_int == 4:
    #         name = "access_token_charlie"

    print(" "*100, end="\r", flush=True)
    print(f"pay name: {name}, index: {index}", end="\r", flush=True)
    chatbot = Chatbot(config={"access_token": config[name]})
    return chatbot


def get_free_chatbot(index):
    # print('free index: ', index)
    free_count = 3
    name = ""
    if index % free_count == 0:
        name = "access_token_r105"
    elif index % free_count == 1:
        name = "access_token_vic_yy"
    elif index % free_count == 2:
        name = "access_token_tony"
    
    print(" "*100, end="\r", flush=True)
    print(f"free name: {name}, index: {index}", end="\r", flush=True)
    chatbot = Chatbot(config={"access_token": config[name]})
    return chatbot


def load_data(DATASET):
    return pd.read_json(DATASET)


def find_foreign_keys_MYSQL_like(db_name):
    df = spider_foreign[spider_foreign["Database name"] == db_name]
    output = "["
    for index, row in df.iterrows():
        output += (
            row["First Table Name"]
            + "."
            + row["First Table Foreign Key"]
            + " = "
            + row["Second Table Name"]
            + "."
            + row["Second Table Foreign Key"]
            + ","
        )
    output = output[:-1] + "]"
    return output


def find_fields_MYSQL_like(db_name):
    df = spider_schema[spider_schema["Database name"] == db_name]
    df = df.groupby(" Table Name")
    output = ""
    for name, group in df:
        output += "Table " + name + ", columns = ["
        for index, row in group.iterrows():
            output += row[" Field Name"] + ","
        output = output[:-1]
        output += "]\n"
    return output


def find_primary_keys_MYSQL_like(db_name):
    df = spider_primary[spider_primary["Database name"] == db_name]
    output = "["
    for index, row in df.iterrows():
        output += row["Table Name"] + "." + row["Primary Key"] + ","
    output = output[:-1]
    output += "]\n"
    return output


def creatiing_schema(DATASET_JSON):
    schema_df = pd.read_json(DATASET_JSON)
    schema_df = schema_df.drop(["column_names", "table_names"], axis=1)
    schema = []
    f_keys = []
    p_keys = []
    for index, row in schema_df.iterrows():
        tables = row["table_names_original"]
        col_names = row["column_names_original"]
        col_types = row["column_types"]
        foreign_keys = row["foreign_keys"]
        primary_keys = row["primary_keys"]
        for col, col_type in zip(col_names, col_types):
            index, col_name = col
            if index == -1:
                for table in tables:
                    schema.append([row["db_id"], table, "*", "text"])
            else:
                schema.append([row["db_id"], tables[index], col_name, col_type])
        for primary_key in primary_keys:
            index, column = col_names[primary_key]
            p_keys.append([row["db_id"], tables[index], column])
        for foreign_key in foreign_keys:
            first, second = foreign_key
            first_index, first_column = col_names[first]
            second_index, second_column = col_names[second]
            f_keys.append(
                [
                    row["db_id"],
                    tables[first_index],
                    tables[second_index],
                    first_column,
                    second_column,
                ]
            )
    spider_schema = pd.DataFrame(
        schema, columns=["Database name", " Table Name", " Field Name", " Type"]
    )
    spider_primary = pd.DataFrame(
        p_keys, columns=["Database name", "Table Name", "Primary Key"]
    )
    spider_foreign = pd.DataFrame(
        f_keys,
        columns=[
            "Database name",
            "First Table Name",
            "Second Table Name",
            "First Table Foreign Key",
            "Second Table Foreign Key",
        ],
    )
    return spider_schema, spider_primary, spider_foreign


def debuger(test_sample_text, database, sql):
    instruction = """#### For the given question, use the provided tables, columns, foreign keys, and primary keys to fix the given SQLite SQL QUERY for any issues. If there are any problems, fix them. If there are no issues, return the SQLite SQL QUERY as is.
#### Use the following instructions for fixing the SQL QUERY:
1) Use the database values that are explicitly mentioned in the question.
2) Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
3) Use DESC and DISTINCT when needed.
4) Pay attention to the columns that are used for the GROUP BY statement.
5) Pay attention to the columns that are used for the SELECT statement.
6) Only change the GROUP BY clause when necessary (Avoid redundant columns in GROUP BY).
7) Use GROUP BY on one column only.

"""
    fields = find_fields_MYSQL_like(database)
    fields += "Foreign_keys = " + find_foreign_keys_MYSQL_like(database) + "\n"
    fields += "Primary_keys = " + find_primary_keys_MYSQL_like(database)
    prompt = (
        instruction
        + fields
        + "#### Question: "
        + test_sample_text
        + "\n#### SQLite SQL QUERY\n"
        + sql
        + "\n#### SQLite FIXED SQL QUERY\nSELECT"
    )
    return prompt


def GPT4_generation(chatbot, prompt, model="text-davinci-002-render-sha"):
    for data in chatbot.ask(prompt, conversation_id=None, parent_id=None, model=model):
        response = data["message"]
    print(data)
    GPT4_clear_conversations(chatbot)
    return response


def GPT4_debug(chatbot, prompt, model="text-davinci-002-render-sha"):
    for data in chatbot.ask(prompt, conversation_id=None, parent_id=None, model=model):
        response = data["message"]
    print(data)
    GPT4_clear_conversations(chatbot)
    return response


def GPT4_clear_conversations(chatbot):
    chatbot.clear_conversations()


def natsql_prompt_maker(test_sample_text, database, schema_links):
    instruction = "# Use the the schema links to generate the natsql and sql queries for each of the questions.\n"
    fields = find_fields_MYSQL_like("college_2")
    fields += "Foreign_keys = " + find_foreign_keys_MYSQL_like("college_2") + "\n"
    fields += find_fields_MYSQL_like(database)
    fields += "Foreign_keys = " + find_foreign_keys_MYSQL_like(database) + "\n"
    fields += "\n"
    prompt = (
        instruction
        + fields
        + resd_prompt
        # + 'Q: "'
        # + test_sample_text
        + "\ninput = "
        + schema_links
        + "\nnatsql = "
        # + natsql
        # + "\nSQL = "
    )
    return prompt


def with_natsql_prompt_maker(test_sample_text, database, schema_links, natsql):
    instruction = "# Use the the schema links and natsql to generate sql queries for each of the questions.\n"
    fields = find_fields_MYSQL_like("college_2")
    fields += "Foreign_keys = " + find_foreign_keys_MYSQL_like("college_2") + "\n"
    fields += find_fields_MYSQL_like(database)
    fields += "Foreign_keys = " + find_foreign_keys_MYSQL_like(database) + "\n"
    fields += "\n"
    prompt = (
        instruction
        + fields
        + resd_prompt
        # + 'Q: "'
        # + test_sample_text
        + "\ninput = "
        + schema_links
        + "\nnatsql = "
        + natsql
        + "\nSQL = "
    )
    return prompt


spider_schema, spider_primary, spider_foreign = creatiing_schema(DATASET_SCHEMA)
val_df = load_data(DATASET)
schema_link_info_list = load_schema_link_list(SCHEMA_LINK_PATH)
crt_time = time.strftime("%m-%d-%H:%M:%S", time.localtime())
print(f"Number of data samples {val_df.shape[0]}")
start_index = 51
end_index = 400
pay_index = 0
except_count = 0

with open(
    f"{FILE_PATH}/gpt-4/2/resd_record-{start_index}-{end_index}-{crt_time}.log", "w"
) as record, open(
    f"{FILE_PATH}/gpt-4/2/resd_predicted_sql-{start_index}-{end_index}-{crt_time}.log",
    "w",
) as predicted:
    CODEX = []
    for (index, row), schema_links in zip(val_df.iterrows(), schema_link_info_list):
        if index < start_index:
            continue  # for testing
        print("index:", index)
        # if index < 10: continue #for testing
        record.write(f"\nindex is {index}" + "\n")
        record.write(row["query"] + "\n")
        record.write(row["question"] + "\n")
        record.write("schema_links:" + "\n")
        record.write(schema_links + "\n")
        print("run SQL generation ...", flush=True)
        SQL = None
        while SQL is None:
            try:
                SQL = GPT4_generation(
                    get_pay_chatbot(pay_index),
                    natsql_prompt_maker(row["question"], row["db_id"], schema_links),
                    config["model"],
                )
                pay_index += 1
                except_count = 0
            except:
                pay_index += 1
                except_count += 1
                time.sleep(3)
                if except_count > 25:
                    print("except too many times, sleep for 3600 second, current time:", time.strftime("%m-%d-%H:%M:%S", time.localtime()))
                    time.sleep(3600)
                    except_count = 0
                pass
        # try:
        #     SQL = SQL.split("SQL: ")[1]
        # except:
        #     record.write("SQL slicing error" + "\n")
        #     SQL = "SELECT"
        # if not SQL.startswith('SELECT'):
        #     SQL = 'SELECT ' + SQL
        record.write("natsql and SQL generation:" + "\n")
        record.write(SQL + "\n")
        natsql = SQL.split("SQL = ")[0]
        record.write("natsql:" + "\n")
        record.write(natsql + "\n")
        try:
            SQL = SQL.split("SQL = ")[1]
        except:
            # SQL = natsql
            try:
                SQL = GPT4_generation(
                    get_pay_chatbot(pay_index),
                    with_natsql_prompt_maker(
                        row["question"], row["db_id"], schema_links, natsql
                    ),
                    config["model"],
                )
                pay_index += 1
                except_count = 0
            except:
                pay_index += 1
                except_count +=1
                time.sleep(3)
                if except_count > 25:
                    print("except too many times, sleep for 3600 second, current time:", time.strftime("%m-%d-%H:%M:%S", time.localtime()))
                    time.sleep(3600)
                    except_count = 0
                pass
        finally:
            record.write("SQL:" + "\n")
            record.write(SQL + "\n")
        print("run self correction ...", flush=True)
        debugged_SQL = None
        while debugged_SQL is None:
            try:
                debugged_SQL = GPT4_debug(
                    get_pay_chatbot(pay_index),
                    debuger(row["question"], row["db_id"], SQL),
                    config["model"],
                ).replace("\n", " ")
                pay_index += 1
            except:
                pay_index += 1
                time.sleep(3)
                pass
        # if debugged_SQL.startwith('SELECT') and debugged_SQL != 'SELECT':
        #     SQL = debugged_SQL
        # elif debugged_SQL == 'SELECT':
        #     pass
        # else:
        SQL = "SELECT " + debugged_SQL
        record.write("self correction:" + "\n")
        record.write(SQL + "\n")
        predicted.write(SQL + "\n")
        CODEX.append([row["question"], SQL, row["query"], row["db_id"]])
        if index == end_index:
            break

        if index % 75 == 0 and index != 0:
            print("sleep for 3600 second, current time:", time.strftime("%m-%d-%H:%M:%S", time.localtime()))
            time.sleep(3600)