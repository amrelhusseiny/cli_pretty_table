import os
# testing Help command
print('#################### testing Help ###########################')
os.system('python cli_pretty_table/cli_pretty_table.py --help')
# testing the comand line functionality 
print('#################### testing json_raw ###########################')
os.system('python cli_pretty_table/cli_pretty_table.py --json_raw \'[{"name":"amr","age":"20"},{"name":"hamed","age":"32"}]\'')

