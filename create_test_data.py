import random
import json
import string


with open('customer_master_parameters.json') as data_file:
    data = json.load(data_file)
separator=(data["separator"])


def create_row(column_definations):
    row_value = ""
    for x in column_definations:

        # each if block if for datatype. You can add your own datatypes
        # e.g. datatype == "email" can be string.ascii_letters + string.digits + '@'
        if x["datatype"] == "string":
            if x["is_variable_legth"]:
                if x["is_null"]:
                    ll = random.randint(0, x["length"])
                else:
                    ll = random.randint(1, x["length"])
            else:
                ll = x["length"]
            value_of_string = ''.join(random.choice(string.ascii_letters + string.digits + 'äëöü') for _ in range(ll))

        ####################
        elif x["datatype"] == "file":
            f = open(x["file_path"], encoding="utf8")
            test = []
            for row in f:
                test.append(row.rstrip("\n"))
            value_of_string = random.choice(test)
        ####################

        if row_value == "":
            row_value = value_of_string
        else:
            row_value = row_value + separator + value_of_string
    return (row_value)


f = open(data["filename"],'w',encoding="utf8")
for i in range(data["number_of_rows"]):
    each_row=create_row(data["columns"]).rstrip('\n')
    print(each_row ,file=f)
f.close()
