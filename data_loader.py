import csv
import os


def load_csv(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError("Dataset not found!")

    with open(file_path, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        headers = reader.fieldnames

        if not headers:
            raise ValueError("CSV file has no headers!")

        rows = list(reader)

    return headers, rows
  
