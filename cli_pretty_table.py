# cli_pretty_table.py

# Non-standard library 
from texttable import Texttable
# Standard Library 
import argparse
import json
import sys

def cli_pretty_table(list_of_dictionaries):
    table = Texttable(max_width=100)

    # Adding Column names to table
    column_names = []
    for item in list_of_dictionaries:
        for key_name in item.keys():
            if key_name not in column_names:
                column_names.append(key_name)
    table.add_row(column_names)
    # Adding data to the table : 
    for item in list_of_dictionaries:
        row_to_add = []
        for cell in column_names : 
            # Usig exception handling to avoid error if column does not exist in a row 
            try:
                row_to_add.append(item[cell])
            except:
                row_to_add.append('')
        table.add_row(row_to_add)
    print(table.draw())
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", help="input a list of dictionaries")
    args = parser.parse_args()
    print(json.loads(args.json))
    # Main for testing the scipt :     
    # cli_pretty_table(args.json)

if __name__ == "__main__":
    main()