from revChatGPT.V1 import Chatbot
import random
import json
f = open('config.json')
config = json.load(f)
config['model'] = "gpt-4"

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
    print(f'free name: {name}, index: {index}', end='\r', flush=True)
    chatbot = Chatbot(config={"access_token": config[name]})
    return chatbot

def get_pay_chatbot(index):
    # print('pay index: ', index)
    pay_count = 4
    name = ""
    if index % pay_count == 0:
        name = 'access_token_vic'
    elif index % pay_count == 1:
        name = 'access_token_3744'
    elif index % pay_count == 2:
        name = 'access_token_lab'
    elif index % pay_count == 3:
        name = "access_token_charlie"
        # rand_int = random.randrange(5) 
        # # 為了讓這隻帳號不要被跑太多次
        # if rand_int == 0:
        #     name = "access_token_lab"
        # elif rand_int == 1:
        #     name = "access_token_lab"
        # elif rand_int == 2:
        #     name = "access_token_vic"
        # elif rand_int == 3:
        #     name = "access_token_charlie"
        
    print(f'pay name: {name}, index: {index}', end='\r', flush=True)
    chatbot = Chatbot(config={"access_token": config[name]})
    return chatbot

import pandas as pd
import time
import os
import sys

tmp_config = {
    "dateset": "./data/",
    "output": "predicted_sql.txt"
}
# if sys.argv[1] == "--dataset" and sys.argv[3] == "--output":
DATASET_SCHEMA = tmp_config['dateset']+"tables.json"
DATASET = tmp_config['dateset']+"dev.json"
OUTPUT_FILE = tmp_config['output']
FILE_PATH = 'my_result/resqsql/gpt-4'
BEFORE_SQL = f"{FILE_PATH}/resd_record_get_before.txt"
AFTER_SQL = f"{FILE_PATH}/resd_record_get_after.txt"

def load_data(DATASET):
  return pd.read_json(DATASET)

def load_sql_txt(file_path):
  with open(file_path, 'r') as f:
    return [line.strip() for line in f]

def find_foreign_keys_MYSQL_like(db_name):
  df = spider_foreign[spider_foreign['Database name'] == db_name]
  output = "["
  for index, row in df.iterrows():
    output += row['First Table Name'] + '.' + row['First Table Foreign Key'] + " = " + row['Second Table Name'] + '.' + row['Second Table Foreign Key'] + ','
  output= output[:-1] + "]"
  return output
def find_fields_MYSQL_like(db_name):
  df = spider_schema[spider_schema['Database name'] == db_name]
  df = df.groupby(' Table Name')
  output = ""
  for name, group in df:
    output += "Table " +name+ ', columns = ['
    for index, row in group.iterrows():
      output += row[" Field Name"]+','
    output = output[:-1]
    output += "]\n"
  return output
def find_primary_keys_MYSQL_like(db_name):
  df = spider_primary[spider_primary['Database name'] == db_name]
  output = "["
  for index, row in df.iterrows():
    output += row['Table Name'] + '.' + row['Primary Key'] +','
  output = output[:-1]
  output += "]\n"
  return output
def creatiing_schema(DATASET_JSON):
    schema_df = pd.read_json(DATASET_JSON)
    schema_df = schema_df.drop(['column_names','table_names'], axis=1)
    schema = []
    f_keys = []
    p_keys = []
    for index, row in schema_df.iterrows():
        tables = row['table_names_original']
        col_names = row['column_names_original']
        col_types = row['column_types']
        foreign_keys = row['foreign_keys']
        primary_keys = row['primary_keys']
        for col, col_type in zip(col_names, col_types):
            index, col_name = col
            if index == -1:
                for table in tables:
                    schema.append([row['db_id'], table, '*', 'text'])
            else:
                schema.append([row['db_id'], tables[index], col_name, col_type])
        for primary_key in primary_keys:
            index, column = col_names[primary_key]
            p_keys.append([row['db_id'], tables[index], column])
        for foreign_key in foreign_keys:
            first, second = foreign_key
            first_index, first_column = col_names[first]
            second_index, second_column = col_names[second]
            f_keys.append([row['db_id'], tables[first_index], tables[second_index], first_column, second_column])
    spider_schema = pd.DataFrame(schema, columns=['Database name', ' Table Name', ' Field Name', ' Type'])
    spider_primary = pd.DataFrame(p_keys, columns=['Database name', 'Table Name', 'Primary Key'])
    spider_foreign = pd.DataFrame(f_keys,
                        columns=['Database name', 'First Table Name', 'Second Table Name', 'First Table Foreign Key',
                                 'Second Table Foreign Key'])
    return spider_schema,spider_primary,spider_foreign

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


def new_debuger(test_sample_text,database,sql):
  instruction = """#### For the given question, use the provided tables, columns, foreign keys, and primary keys to fix the given SQLite SQL QUERY for any issues. If there are any problems, fix them. If there are no issues, return the SQLite SQL QUERY as is.
#### Use the following instructions for fixing the SQL QUERY:
1) Use the database values that are explicitly mentioned in the question.
2) Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
3) Use DESC and DISTINCT when needed.
4) Pay attention to the columns that are used for the GROUP BY statement when using SUM, AVG, MAX, MIN and COUNT.
5) Pay attention to the columns that are used for the SELECT statement.
6) Only change the GROUP BY clause when necessary (Avoid redundant columns in GROUP BY).
7) Use GROUP BY on one column only.

"""
  fields = find_fields_MYSQL_like(database)
  fields += "Foreign_keys = " + find_foreign_keys_MYSQL_like(database) + '\n'
  fields += "Primary_keys = " + find_primary_keys_MYSQL_like(database)
  prompt = instruction + fields+ '#### Question: ' + test_sample_text + '\n#### SQLite SQL QUERY\n' + sql +'\n#### SQLite FIXED SQL QUERY\nSELECT'
  return prompt

def codex_debuger(test_sample_text,database,sql):
  instruction = '##### Fix bugs in the below SQL for the given question.\n'
  fields = find_fields_MYSQL_like(database)
  fields += "Foreign_keys = " + find_foreign_keys_MYSQL_like(database) + '\n'
  fields += "Primary_keys = " + find_primary_keys_MYSQL_like(database)
  prompt = fields + instruction + '### ' + test_sample_text + '\n#### Buggy SQL\n' + sql +'\n#### Fixed SQL\nSELECT'
  return prompt

def GPT4_debug(chatbot, prompt, model="text-davinci-002-render-sha"):
    for data in chatbot.ask(prompt, conversation_id=None, parent_id=None, model=model):
        response = data["message"]
    GPT4_clear_conversations(chatbot)
    return response

def GPT4_clear_conversations(chatbot):
  chatbot.clear_conversations()

# time.sleep(7200)
spider_schema,spider_primary,spider_foreign = creatiing_schema(DATASET_SCHEMA)
val_df = load_data(DATASET)
before_SQL_list = load_sql_txt(BEFORE_SQL)
after_SQL_list = load_sql_txt(AFTER_SQL)
crt_time = time.strftime("%m-%d-%H:%M:%S", time.localtime())
print(f"Number of data samples {val_df.shape[0]}")
start_index = 566
end_index = 1033
free_index = 0
pay_index = 0
with open(f'{FILE_PATH}/my_correction_record-({start_index}-{end_index})-{crt_time}.log', 'w') as record, open(f'{FILE_PATH}/my_correction_predicted_sql-({start_index}-{end_index})-{crt_time}.log', 'w') as pred:
    # CODEX = []
    for ((index, row), before_SQL, after_SQL) in zip(val_df.iterrows(), before_SQL_list, after_SQL_list):
        if index < start_index: continue #for testing
        print("index:", index)
        # if index < 10: continue #for testing
        record.write(f"\nindex is {index}"+ '\n')
        record.write(row['query']+ '\n')
        record.write(row['question']+ '\n')
        
        record.write('SQL generation:'+ '\n')
        record.write(before_SQL+ '\n')

        if after_SQL.lower().startswith('select the ') or after_SQL == '':
          debugged_SQL = None
        else:
          debugged_SQL = after_SQL
        while debugged_SQL is None:
            try:
                rand_int = random.randrange(3)
                if False:#rand_int < 2: 
                  chatbot = get_free_chatbot(free_index)
                else:
                  chatbot = get_pay_chatbot(pay_index)
                  pay_index+=1
                #正常
                with open (f'{FILE_PATH}/debug_prompt.txt', 'w') as f:
                   f.write(new_debuger(row['question'], row['db_id'], before_SQL))
                # debugged_SQL = GPT4_debug(chatbot,debuger(row['question'], row['db_id'], before_SQL), config['model']).replace("\n", " ")
                
                
                # 我的版
                debugged_SQL = GPT4_debug(chatbot,new_debuger(row['question'], row['db_id'], before_SQL), config['model']).replace("\n", " ")
                if debugged_SQL.lower().startswith('the ') or debugged_SQL.strip() == '':
                  debugged_SQL = before_SQL
                # Codex版
                # with open (f'{FILE_PATH}/debug_prompt.txt', 'w') as f:
                #    f.write(codex_debuger(row['question'], row['db_id'], SQL))
                # debugged_SQL = ' '
                # debugged_SQL = GPT4_debug(chatbot,codex_debuger(row['question'], row['db_id'], SQL)).replace("\n", " ")
                  
                # free_index += 1
            except:
                # free_index += 1
                # print("except: sleep for 210 second, current time:", time.strftime("%m-%d-%H:%M:%S", time.localtime()))
                time.sleep(3)
                pass
        if debugged_SQL.lower().startswith('select'):
          SQL = debugged_SQL
        else:
          SQL = "SELECT " + debugged_SQL
        record.write('self correction:'+ '\n')
        record.write(SQL+ '\n')
        pred.write(SQL + '\n')
        # CODEX.append([row['question'], SQL, row['query'], row['db_id']])
        #break
        # if index % 100 == 0 and index != 0: 
        #    print("sleep for 140 second, current time:", time.strftime("%m-%d-%H:%M:%S", time.localtime()))
        #    time.sleep(140)
        if index == end_index: break