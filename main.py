import sys

from lib.get_pqc_data import get_pqc_data
from lib.parse_input import parse_input
from lib.validate_types import validate_types
from lib.write_to_csv import write_to_csv


def main():
    input_path, output_path, types_as_int = validate_types(sys.argv[1:])
    company_numbers = parse_input(input_path)
    data = get_pqc_data(company_numbers, types_as_int)
    write_to_csv(data, output_path)


main()
