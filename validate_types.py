import sys
from typing import List
from pathlib import Path

def validate_types(types: List[str]):
    if len(types) != 2:
        print("Usage: python3 main.py <input_file> <output_file>")
        sys.exit(1)

    input_path, output_path = types
    input_path, output_path = Path(input_path).resolve(), Path(output_path).resolve()

    if not input_path.is_file():
        print("Input file does not exist")
        sys.exit(1)

    return input_path, output_path

