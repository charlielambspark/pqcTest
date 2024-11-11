import sys

from lib.get_personal_insolvencies_data import get_personal_insolvencies_data
from lib.parse_input import parse_input
from lib.validate_types import validate_types
from lib.write_personal_insolvencies import write_personal_insolvencies


def get_personal_insolvencies():
    input_path, output_path, types_as_int = validate_types(sys.argv[1:])
    company_numbers = parse_input(input_path)
    data = get_personal_insolvencies_data(company_numbers)
    write_personal_insolvencies(data, output_path)


get_personal_insolvencies()
