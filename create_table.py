import connector
from get_data import get_csv_data

cur = connector.cur
table_name = 'bigData'
csv_data = get_csv_data()

def has_table(name)->bool:
    cur.execute(f'SHOW TABLES LIKE "{name}"')
    result = cur.fetchone()
    return result


def create_table(name, csv_data.column_name, csv_data.values_type):
    if not has_table(table_name):
        s = f"create table {table_name} ({csv_data.column_name[0]} {csv_data.values_type[0]});"
        cur.execute(s)

    print(f"{name} exist in database.")
    for i in range(1, len(csv_data.column_name)):
        try:
            s = f"alter table {name} add ({csv_data.column_name[i]} {csv_data.values_type[i]});"
            cur.execute(s)
        except:
            print(f"You already have column with name {csv_data.column_name[i]}")


create_table(table_name, csv_data.column_name, csv_data.values_type)
