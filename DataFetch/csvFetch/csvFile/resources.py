import csv
from .models import Parking


def import_data_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row if present
        for row in csv_reader:
            Parking.objects.create(
                Frame_Number=row[0],
                Spot_Index=row[1],
                Spot_Status=row[2]
            )
