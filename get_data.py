import csv

csv_file = "Individual_Incident_2004.csv"

csv_data = csv.reader(open(csv_file))

columns_name = next(csv_data)
values_type = []
for row in next(csv_data):
    try:
        int(row)
    except ValueError:
        values_type.append('longtext')
    else:
        # must be change
        values_type.append('longtext')


def get_lines_count(csv_data):
    lines = len(list(csv_data))
    return lines


csv_data = csv.reader(open(csv_file))
print("Getting csv lines count ...")
rows_count = get_lines_count(csv_data) - 1
print("Csv lines count get")