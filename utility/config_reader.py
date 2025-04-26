import json
import sys
from typing import List
from interface.delete_config_type import DeleteConfigType

def load_config(file_loc: str) -> List[DeleteConfigType]:
    try:
        with open(file_loc, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"[ERROR]: \"{file_loc}\" not found. Please make sure the file exists.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"[ERROR]: \"{file_loc}\" is not a valid JSON file.")
        sys.exit(1)

        