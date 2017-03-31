import pandas as pd
import json
import shutil

with open('customer_master_parameters.json') as data_file:
    data = json.load(data_file)
separator=(data["separator"])

def give_index_number_of_column(column_name):
    for index,col_name in enumerate(data["columns"]):
        if column_name == col_name["column_name"]:
            return index


def rectify_greater_than(file_name, column_1, column_2):
    # take the column name and get the index number from the data["columns"] list
    first = give_index_number_of_column(column_1)
    second = give_index_number_of_column(column_2)

    test_data = pd.read_csv(file_name, header=None, encoding="utf8", index_col=False, dtype=str)
    idx = test_data[first] > test_data[second]
    test_data.loc[idx, [first, second]] = test_data.loc[idx, [second, first]].values
    test_data.to_csv(file_name, header=None, index=False, encoding="utf8")


def backup_file(file_name):
    bakupfilename = file_name + ".bgt"
    shutil.copyfile(file_name,bakupfilename)



backup_file(data["filename"])

for rules in data["cleanup_rules"]:
    if "greater_than" in rules.keys() :
        rectify_greater_than(data["filename"],rules["greater_than"][0],rules["greater_than"][1])