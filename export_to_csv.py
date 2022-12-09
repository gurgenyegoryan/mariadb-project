import connector
import create_table

table_name = create_table.table_name
cur = connector.cur


def fetch_table_data(table_name):
    cur.execute('select * from ' + table_name)

    header = [row[0] for row in cur.description]

    rows = cur.fetchall()

    # Closing connection
    cur.close()

    return header, rows


def export(table_name):
    header, rows = fetch_table_data(table_name)

    # Create csv file
    f = open(table_name + '.csv', 'w')

    # Write header
    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')

    f.close()
    print(str(len(rows)) + ' rows written successfully to ' + f.name)


export(table_name)
