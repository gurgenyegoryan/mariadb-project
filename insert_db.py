import create_table
import get_data
import connector
import mariadb
import datetime
import time
from time import sleep
import threading

csv_data = get_data.csv_data
table_name = create_table.table_name
columns_name = get_data.columns_name
values_count = len(columns_name) * '?,'
values_count = values_count.rstrip(values_count[-1])

columns_name_string = ','.join([str(item) for item in columns_name])



# start = time.time()

counter = 0
start = 0

def insert_process(data, tb_name, cl_name_string, vl_count):
    global counter, current, start
    start = time.time()
    current = datetime.datetime.now()
    print(f"Process started {current}")
    for row in data:
        try:
            connector.cur.execute(f"INSERT INTO {tb_name} ({cl_name_string}) VALUES ({vl_count})", row)
            counter += 1
            # print('row set: ')

        except mariadb.Error as e:
            print(f"Error: {e}")


def counter_rows():
    j = 1
    while j < 10:
        print(counter)
        time.sleep(1)

        j += 1




threading.Thread(target=insert_process, args=(csv_data, table_name, columns_name_string, values_count)).start()
threading.Thread(target=counter_rows()).start()

current = datetime.datetime.now()
print(f"Process ended {current}")
end = time.time()
timer = end - start
print(f"Process to last {timer / 60} minutes")
