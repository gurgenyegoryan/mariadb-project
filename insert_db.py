import os
import time
import datetime
import threading

import mariadb
import connector

import create_table
from get_data import get_csv_data

cur = connector.cur
csv_get = get_csv_data()
table_name = create_table.table_name
columns_name = csv_get.columns_name
values_count = len(columns_name) * '?,'
values_count = values_count.rstrip(values_count[-1])
columns_name_string = ','.join([str(item) for item in columns_name])
rows_count = csv_get.rows_count
csv_data = csv_get.data


def insert_process(data, tb_name, cl_name_string, vl_count):
    global counter, current

    start = time.time()
    current = datetime.datetime.now()
    print(f"Process started {current}")

    for row in data:
        try:
            cur.execute(f"INSERT INTO {tb_name} ({cl_name_string}) VALUES ({vl_count})", row)
        except mariadb.Error as e:
            print(f"Error: {e}")

    current = datetime.datetime.now()
    print(f"Process ended {current}")

    end = time.time()
    timer = end - start
    speed = rows_count / timer
    print(f"Process to last {timer / 60} minutes")
    print(f"Inserting speed is {speed} r/s, where <r> is row, <s> is second.")

    cur.close()


def get_using_ram():
    ram_usage = []
    while thread_insert.is_alive():
        # Getting all memory using os.popen()
        total_memory, used_memory, free_memory = map(
         int, os.popen('free -t -m').readlines()[-1].split()[1:])
        ram_usage.append(used_memory)
        time.sleep(1)
    print(ram_usage[1:20])



thread_insert = threading.Thread(target=insert_process, args=(csv_data, table_name, columns_name_string, values_count))
thread_get_ram = threading.Thread(get_using_ram())

thread_insert.start()
thread_get_ram.start()