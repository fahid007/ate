import csv
with open ('script1.csv', 'r') as csv_file:
    csv_reader= csv.reader(csv_file)
    next(csv_reader)
    my_dict={}
    for line in csv_reader:
        my_dict[line[0]]=line[1]
print(my_dict)
for keys, values in my_dict.items():
    print("key:",keys, "|", "Value:", values)