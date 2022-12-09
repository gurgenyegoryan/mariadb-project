import connector
import create_table

import csv
import sys

table_name = create_table.table_name
cur = connector.cur


# def fetch_table_data(table_name):
#     cur.execute('select * from ' + table_name)
#
#     header = [row[0] for row in cur.description]
#
#     rows = cur.fetchall()
#
#     # Closing connection
#     cur.close()
#
#     return header, rows
#
#
# def export(table_name):
#     header, rows = fetch_table_data(table_name)
#
#     # Create csv file
#     f = open(table_name + '.csv', 'w')
#
#     # Write header
#     f.write(','.join(header) + '\n')
#
#     for row in rows:
#         f.write(','.join(str(r) for r in row) + '\n')
#
#     f.close()
#     print(str(len(rows)) + ' rows written successfully to ' + f.name)
#
#
# export(table_name)


sql = f'SELECT * from {table_name}'
csv_file_path = 'my_csv_file.csv'

try:
    cur.execute(sql)
    rows = cur.fetchall()
finally:
    cur.close()

# Continue only if there are rows returned.
if rows:
    # New empty list called 'result'. This will be written to a file.
    result = list()

    # The row name is the first entry for each entity in the description tuple.
    column_names = list()
    for i in cur.description:
        column_names.append(i[0])

    result.append(column_names)
    for row in rows:
        result.append(row)

    # Write result to file.
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in result:
            csvwriter.writerow(row)
else:
    sys.exit("No rows found for query: {}".format(sql))
