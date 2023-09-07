import csv
mydict={}
jobs=['engineer', 'operator', 'administrator']
def clear(a):
    b=a.copy()
    for keys in a:
        job=a[keys]
        for i in job:
            if i not in jobs:
                job.remove(i)
        b[keys]=job
    return(b)
with open('script3.csv', 'r')as csvfil:
    csvred= csv.reader(csvfil)
    next(csvred)
    for line in csvred:
        mydict[line[0]]= line[1:]
for key, values in mydict.items():
    print("Name:", key, "|", "Jobs:", values)
mydict=clear(mydict)
print("Cleared Dictionary:")
for key, values in mydict.items():
    print("Name:", key, "|", "Jobs:", values)
while True:
    a=input("Name:")
    b=input("Job:")
    if a not in mydict.keys():
        print("No account")
        x = int(input("Continue?"))
        if x == 0:
            break
    else:
        if str(b) in mydict[a]:
            print("True")
        else:
            print("False")
    x=int(input("Continue?"))
    if x==0:
        break