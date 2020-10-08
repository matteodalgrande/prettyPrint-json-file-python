################################# APRIRE FILE, LEGGERE, SCRIVERE E SOVRASCRIVERLO###########################################
import json
import sys

num_arg = int(len(sys.argv))
list_arg = sys.argv

if num_arg == int(2):
    name_file = str(list_arg[1])
    print(list_arg[1])
    with open(name_file, 'r') as f:
        t = f.read()
        parsed_json = json.loads(str(t))
        indent_json = json.dumps(parsed_json, indent=4, sort_keys=True)
        f.close()
    with open(name_file, 'w+') as f:
        f.write(indent_json)
        f.close()
else:
    print('Error: number of elemet need to has equals 2')
    print('###### ex.')
    print('###### prettyPrint-json-file-python.py file_path_or_name')