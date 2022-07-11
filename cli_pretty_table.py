# cli_pretty_table.py

# Non-standard library 
from texttable import Texttable
# Standard Library 
import argparse
import json
import sys
import re

def cli_pretty_table(list_of_dictionaries):
    table = Texttable(max_width=120)

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
    parser.add_argument("--json_raw", help="input a list of dictionaries - example '[{\"name\":\"amr\",\"age\":\"20\"}]' ")
    parser.add_argument("--json_file", help="input json file path")
    args = parser.parse_args()
    # Confirm command has input 
    if not any(vars(args).values()):
        raise ValueError('invalid input , type --help')
    # Add list bracket if not present in input
    input_string = args.json_raw
    input_string = input_string.replace(' ','')
    input_string = input_string.replace('\r','')
    input_string = input_string.replace('\n','')
    print(input_string)
    if not re.match(r"^\[",input_string) and not re.match(r"\]$",input_string):
        input_string = '['+input_string+']'
    else:
        input_string = input_string
    # Confirm correct json format 
    try:
        json.parse(input_string)
    except :
        raise ValueError('invalid json format')
    input_data = json.loads(input_string)
    # Main for testing the scipt :     
    cli_pretty_table(input_data)

if __name__ == "__main__":
    main()