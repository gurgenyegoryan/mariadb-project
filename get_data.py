import csv


csv_file = "Individual_Incident_2004.csv"
with open(csv_file) as file_obj:
    # Get columns name
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


