import csv
import _csv

from dataclasses import dataclass, is_dataclass


@dataclass
class CSVData:
    data: _csv.reader = None
    columns_name = []
    values_type = []
    rows_count = 0


csv_data = CSVData()


def get_csv_data() -> CSVData:
    csv_file = "Individual_Incident_2004.csv"
    csv_data.data = csv.reader(open(csv_file))
    csv_data.rows_count = len(list(csv.reader(open(csv_file))))
    csv_data.columns_name = next(csv_data.data)

    for row in csv_data.data:
        for cell in row:
            try:
                int(cell)
            except ValueError:
                csv_data.values_type.append('longtext')
            else:
                csv_data.values_type.append('longtext')
        break

    return csv_data

