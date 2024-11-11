import csv
from typing import List


def write_personal_insolvencies(data: List[List[str]], output_path: str):
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
        csvfile.close()
