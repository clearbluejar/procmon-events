import sys
from procmon_parser import load_configuration, dump_configuration, Rule

with open(sys.argv[1], "rb") as f:
    config = load_configuration(f)

for key,val in config.items():
    if key == 'FilterRules' or key == 'ColumnMap':
        for item in config[key]:
            if "Column.NONE" in str(item):
                continue
            print(item)
    else:
        print(key,val)