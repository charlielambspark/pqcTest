import sys
from typing import List
from pathlib import Path


def validate_types(types: List[str]):
    if len(types) not in [2, 3]:
        exit_with_comments()
    input_path, output_path = types[0], types[1]
    input_path, output_path = Path(input_path).resolve(), Path(output_path).resolve()

    if not input_path.is_file():
        print("Input file does not exist")
        sys.exit(1)

    types_as_int = True
    if len(types) == 3:
        if types[2] == '--text':
            types_as_int = False
        else:
            exit_with_comments()

    return input_path, output_path, types_as_int


def exit_with_comments():
    print("Usage: python3 main.py <input_file> <output_file>")
    print("Flags: --text (outputs types as text)")
    sys.exit(1)
