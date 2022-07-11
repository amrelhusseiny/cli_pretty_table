# cli_pretty_table.py

# Non-standard library 
from texttable import Texttable
# Standard Library 
import argparse
import json
import sys
import re



def _strip_string(input_string):
    try :
        input_string = str(input_string).replace(' ','')
        input_string = input_string.replace('\r','')
        input_string = input_string.replace('\n','')
    except Exception as e :
        print(e)
    return input_string

def _to_table(list_of_dictionaries):
    table = Texttable(max_width=0)

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
            cell_data = ''
            try:
                row_to_add.append(item[cell])
            except:
                row_to_add.append('')
            # print(cell_data)
        table.add_row(row_to_add)
    print(table.draw())
    # return table.draw()
    return 

def _read_json_file(file_path):
    with open(file_path,'r') as file:
        input_data = json.load(file)
    return input_data

def cli_pretty_table():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_raw", help="input a list of dictionaries - example '[{\"name\":\"amr\",\"age\":\"20\"}]' ")
    parser.add_argument("--json_file", help="input json file path")
    # parser.add_argument("--print_column_names", help="shows the column names of json raw/file so you can choose only to display particular colums")
    args = parser.parse_args()
    # Confirm command has input 
    if not any(vars(args).values()):
        raise ValueError('invalid input , type --help')

    if args.json_raw != None:
        # Add list bracket if not present in input
        input_string = _strip_string(args.json_raw)
        if not re.match(r"^\[",input_string) and not re.match(r"\]$",input_string):
            input_string = '['+input_string+']'
        else:
            input_string = input_string
        # Confirm correct json format 
        try:
            input_data = json.loads(input_string)
        except Exception as e :
            raise ValueError('invalid Json format')
            print(e)
        # Convert to table
        _to_table(input_data)
    elif args.json_file != None : 
        input_data = _read_json_file(args.json_file)
        # Convert to table
        _to_table(input_data)
        

def main():
    cli_pretty_table()

if __name__ == "__main__":
    main()