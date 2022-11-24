import connector
import get_data

cur = connector.cur
column_name = get_data.columns_name
values_type = get_data.values_type
table_name = 'bigData'


def get_tables(name):
    cur.execute(f"SHOW TABLES LIKE '{name}'")
    result = cur.fetchone()
    if result:
        return 0
    else:
        return 1


def create_table(name, column_name, values_type):
    j = 0
    if j < 2:
        if get_tables(table_name) == 1:
            s = f"create table {table_name} ({column_name[0]} {values_type[0]});"
            cur.execute(s)
        else:
            print(f"{name} exist in database.")
            for i in range(1, len(column_name)):
                try:
                    s = f"alter table {name} add ({column_name[i]} {values_type[i]});"
                    cur.execute(s)
                except:
                    print(f"You already have column with name {column_name[i]}")

    j += 1


create_table(table_name, column_name, values_type)


