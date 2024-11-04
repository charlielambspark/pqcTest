import sys

from parse_input import parse_input
from validate_types import validate_types

def main():
    input_path, output_path = validate_types(sys.argv[1:])
    data = parse_input(input_path)
    print(data)

main()