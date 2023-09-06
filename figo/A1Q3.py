import random as rand
a= rand.randint(1, 40)
print("length:", a)
x=[]
for i in range(a):
    x.append(rand.randint(1, 50))
print(x)
for i in x:
    if i <= 10:
        print(i)