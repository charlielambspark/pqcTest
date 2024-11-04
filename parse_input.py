import csv


def parse_input(input_path : str):
    data = []
    try:
        with open(input_path, 'r',) as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row[0])

    except Exception as e:
        print(f"Error reading csv: {str(e)}")

    return data[1:]
