import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
l=[]
for i in a:
    l.append(i)
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            tem=l[j]
            l[j]=l[j+1]
            l[j+1]=tem
# print(l)
b={}
for i in range(len(l)):
    for j in a:
        if l[i]==j:
            b.update({j:a[j]})
# print(b)
d=json.dumps(b)
print(d)