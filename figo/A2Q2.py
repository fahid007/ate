import csv
x=[]
def transpose(x):
    z=[]
    for i in range (len(x[0])):
        y=[]
        for j in range(len(x)):
            y.append(x[j][i])
        z.append(y)
        print(y)
with open('script2.csv', 'r') as csvfile:
    csvrd= csv.reader(csvfile)
    for line in csvrd:
        x.append(line)
        print(line)
    print("\n")
transpose(x)