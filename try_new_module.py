from revChatGPT.V1 import Chatbot
import random
import json
import sqlite3

f = open("config.json")
config = json.load(f)
# config['model'] = "gpt-4"


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
    print(f"free name: {name}, index: {index}", end="\r", flush=True)
    chatbot = Chatbot(config={"access_token": config[name]})
    return chatbot


def get_pay_chatbot(index):
    # print('pay index: ', index)
    pay_count = 4
    name = ""
    if index % pay_count == 0:
        name = "access_token_lab"
    elif index % pay_count == 1:
        name = "access_token_charlie"
    elif index % pay_count == 2:
        name = "access_token_lab"
    elif index % pay_count == 3:
        name = 'access_token_charlie'
        # rand_int = random.randrange(5)
        # # 為了讓這隻帳號不要被跑太多次
        # if rand_int == 0:
        #     name = "access_token_3744"
        # elif rand_int == 1:
        #     name = "access_token_charlie"
        # elif rand_int == 2:
        #     name = "access_token_vic"
        # elif rand_int == 3:
        #     name = "access_token_charlie"

    print(f"pay name: {name}, index: {index}", end="\r", flush=True)
    chatbot = Chatbot(config={"access_token": config[name]})
    return chatbot


import pandas as pd
import time
import os
import sys

tmp_config = {"dateset": "./data/", "output": "predicted_sql.txt"}
# if sys.argv[1] == "--dataset" and sys.argv[3] == "--output":
DATASET_SCHEMA = tmp_config["dateset"] + "tables.json"
DATASET = tmp_config["dateset"] + "dev.json"
OUTPUT_FILE = tmp_config["output"]
FILE_PATH = "my_result/resqsql/3"
BEFORE_SQL = f"{FILE_PATH}/resd_record_get_before.txt"
DB_PATH = "/home/r10525068/ensemble/data/database"
# else:
#     raise Exception("Please use this format python CoT.py --dataset data/ --output predicted_sql.txt")

import re


def remove_non_english(string):
    pattern = r"^[^a-zA-Z]+|[^a-zA-Z]+$"
    cleaned_string = re.sub(pattern, "", string)
    return cleaned_string


def load_data(DATASET):
    return pd.read_json(DATASET)


def load_sql_txt(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f]


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


def find_cols_with_entities_by_sql(SQL):
    sql_str_list = SQL.split(" ")
    sql_str_list = [s for s in sql_str_list if s]
    tb = None
    col = None
    cols_have_entities = []
    for sql_idx, str in enumerate(sql_str_list):
        if (
            str.startswith("'")
            or str.startswith('"')
            or str.startswith("('")
            or str.startswith('("')
        ):
            try:
                tb_col = sql_str_list[sql_idx - 2]
                # print(sql_str_list[sql_idx - 2: sql_idx+1])
                if "." in tb_col:
                    col = remove_non_english(tb_col.split(".")[1]).lower()
                    cols_have_entities.append(col)
                else:
                    col = remove_non_english(tb_col.strip(" ")).lower()
                    cols_have_entities.append(col)
            except:
                print("cannot split it:", sql_str_list[sql_idx - 2])
    return cols_have_entities


def find_table_by_fields(db_name, cols_have_entities):
    df = spider_schema[spider_schema["Database name"] == db_name]
    df = df.groupby(" Table Name")
    tables = {}
    for name, group in df:
        for index, row in group.iterrows():
            if row[" Field Name"].lower() in cols_have_entities:
                col = row[" Field Name"].lower()
                if name not in tables:
                    tables[name] = []
                tables[name].append(col)
    return tables


def find_entities_by_table_fields(db, tables_with_cols):
    connection = sqlite3.connect(f"{DB_PATH}/{db}/{db}.sqlite")
    cursor = connection.cursor()
    cols_with_entities = {}
    for table in tables_with_cols.keys():
        for col in tables_with_cols[table]:
            res = cursor.execute(f"SELECT DISTINCT {col} FROM {table} LIMIT 10")
            value = res.fetchall()
            try:
                int(value[0][0])
            except:
                cols_with_entities[col] = [v[0] for v in value]
    return cols_with_entities


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


def entities_debuger(test_sample_text, database, sql, tables_with_cols):
    instruction = """#### For the given question, use the provided cell values, tables, columns, foreign keys, and primary keys to fix the given SQLite SQL QUERY for any issues. If there are any problems, fix them. If there are no issues, return the SQLite SQL QUERY as is.
#### Use the following instructions for fixing the SQL QUERY:
1) Fix it if entities are similar with cell value below 
2) Use the same rules if cell value below are all lower case or upper case or other rules.
"""
    cols_with_entities = find_entities_by_table_fields(database, tables_with_cols)
    fields = ""
    fields = find_fields_MYSQL_like(database)
    fields += "Foreign_keys = " + find_foreign_keys_MYSQL_like(database) + "\n"
    fields += "Primary_keys = " + find_primary_keys_MYSQL_like(database) + "\n"
    if not cols_with_entities:
        for col in tables_with_cols.keys():
            fields += f"column = [{col}]\n"
            fields += f"type of cell value is number.\n"
    else:
        for col in cols_with_entities.keys():
            fields += f"column = [{col}]\n"
            fields += f"cell value includes [{', '.join(cols_with_entities[col])}]\n"
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


def GPT4_debug(chatbot, prompt, model="text-davinci-002-render-sha"):
    for data in chatbot.ask(prompt, conversation_id=None, parent_id=None, model=model):
        response = data["message"]
    # print(data)
    GPT4_clear_conversations(chatbot)
    return response


def GPT4_clear_conversations(chatbot):
    chatbot.clear_conversations()

# time.sleep(7800)
spider_schema, spider_primary, spider_foreign = creatiing_schema(DATASET_SCHEMA)
val_df = load_data(DATASET)
SQL_list = load_sql_txt(BEFORE_SQL)
crt_time = time.strftime("%m-%d-%H:%M:%S", time.localtime())
print(f"Number of data samples {val_df.shape[0]}")
start_index = 0
end_index = 1034
free_index = 0
pay_index = 0
with open(
    f"{FILE_PATH}/entities_correction/2/entities_correction_record-({start_index}-{end_index})-{crt_time}.log",
    "w",
) as record, open(
    f"{FILE_PATH}/entities_correction/2/entities_correction_predicted_sql-({start_index}-{end_index})-{crt_time}.log",
    "w",
) as before_after, open(
    f"{FILE_PATH}/entities_correction/entities_prompt.txt", "w"
) as entities:
    # CODEX = []
    for (index, row), SQL in zip(val_df.iterrows(), SQL_list):
        if index < start_index:
            continue  # for testing
        print("index:", index)
        # if index < 10: continue #for testing
        record.write(f"\nindex is {index}" + "\n")
        record.write(row["query"] + "\n")
        record.write(row["question"] + "\n")

        record.write("SQL correction:" + "\n")
        record.write(SQL + "\n")
        cols_have_entities = find_cols_with_entities_by_sql(SQL)
        tables_with_cols = find_table_by_fields(row["db_id"], cols_have_entities)
        if not tables_with_cols:
            record.write("original correction:" + "\n")
            record.write(SQL + "\n")
            before_after.write(SQL + "\n")
            pass
        else:
            fixed_entities_SQL = None
            while fixed_entities_SQL is None:
                try:
                    rand_int = random.randrange(3)
                    if True:#rand_int < 2:
                        chatbot = get_free_chatbot(free_index)
                        free_index += 1
                    else:
                        chatbot = get_pay_chatbot(pay_index)
                        pay_index += 1

                    entities.write(
                        entities_debuger(
                            row["question"], row["db_id"], SQL, tables_with_cols
                        )
                        + "\n\n"
                    )
                    fixed_entities_SQL = GPT4_debug(
                        chatbot,
                        entities_debuger(
                            row["question"], row["db_id"], SQL, tables_with_cols
                        ),
                        config['model']
                    ).replace("\n", " ")
                except Exception as e:
                    print(e)
                    # free_index += 1
                    # print("except: sleep for 210 second, current time:", time.strftime("%m-%d-%H:%M:%S", time.localtime()))
                    time.sleep(3)
                    pass
            SQL = "SELECT " + fixed_entities_SQL
            record.write("entities correction:" + "\n")
            record.write(SQL + "\n")
            before_after.write(SQL + "\n")
        if pay_index % 99 == 0 and pay_index != 0:
            print(
                "sleep for 3600 second, current time:",
                time.strftime("%m-%d-%H:%M:%S", time.localtime()),
            )
            time.sleep(3600)
        if index == end_index:
            break
