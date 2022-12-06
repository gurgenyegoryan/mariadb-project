import time
import datetime
import psutil
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

counter = 0
start = 0


def insert_process(data, tb_name, cl_name_string, vl_count):
    global counter, current, start

    start = time.time()
    current = datetime.datetime.now()
    print(f"Process started {current}")

    for row in data:
        try:
            cur.execute(f"INSERT INTO {tb_name} ({cl_name_string}) VALUES ({vl_count})", row)
            counter += 1
            # print('row set: ')
        except mariadb.Error as e:
            print(f"Error: {e}")

    current = datetime.datetime.now()
    print(f"Process ended {current}")

    end = time.time()
    timer = end - start
    speed = timer / rows_count
    print(f"Process to last {timer / 60} minutes")
    print(f"Inserting speed is {speed} r/s, where <r> is row, <s> is second.")

    cur.close()


def get_using_ram():
    ram_list = []
    file = open("text.txt", "a")
    while connector.cur:
        ram_usage = psutil.virtual_memory()[3] / 1000000000
        file.write(str(ram_usage) + '\n')
        time.sleep(0.1)
    file.close()


threading.Thread(target=insert_process, args=(csv_data, table_name, columns_name_string, values_count)).start()
# threading.Thread(target=counter_rows()).start()
threading.Thread(target=get_using_ram())
