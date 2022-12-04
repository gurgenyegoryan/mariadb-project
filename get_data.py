import csv

from dataclasses import dataclass, field

@dataclass
class CSVData:
    data;
    columns_name;
    values_type = []
    rows_count = 0
csv_data = CSVData()


def get_csv_data()->CSVData:
    csv_file = "Individual_Incident_2004.csv"
    csv_data.data = csv.reader(open(csv_file))
    csv_data.columns_name = next(csv_data.data)

    for cell in next(csv_data.data):
        try:
            int(cell)
        except ValueError:
            csv_data.values_type.append('longtext')
        else:
            # must be change
            csv_data.values_type.append('longtext')


    def get_lines_count(csv_data.data):
        lines = len(list(csv_data.data))
        return lines


    csv_data.data = csv.reader(open(csv_file))
    print("Getting csv lines count ...")
    csv_data.rows_count = get_lines_count(csv_data.data) - 1
    print("Csv lines count get")
    return csv_data
