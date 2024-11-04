import sys

from get_pqc_data import get_pqc_data
from parse_input import parse_input
from validate_types import validate_types
from write_to_csv import write_to_csv


def main():
    input_path, output_path = validate_types(sys.argv[1:])
    company_numbers = parse_input(input_path)
    data = get_pqc_data(company_numbers)
    write_to_csv(data,output_path)

main()