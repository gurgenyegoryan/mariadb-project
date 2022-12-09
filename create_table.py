import mariadb

import connector
from get_data import get_csv_data


cur = connector.cur
table_name = 'bigData'
csv_data = get_csv_data()


def has_table(name) -> bool:
    cur.execute(f'SHOW TABLES LIKE "{name}"')
    result = cur.fetchone()
    return result


def create_table(name, columns_name, values_type):
    if not has_table(table_name):
        execute_command = f"create table {name} ({columns_name[0]} {values_type[0]});"
        cur.execute(execute_command)
        print(f"Created {table_name} table")

    print(f"{name} table exist in database.")
    for i in range(1, len(columns_name)):
        try:
            execute_command = f"alter table {name} add ({columns_name[i]} {values_type[i]});"
            cur.execute(execute_command)
        except mariadb.Error as e:
            print(f"You already have column with name {columns_name[i]}: {e}")


create_table(table_name, csv_data.columns_name, csv_data.values_type)
