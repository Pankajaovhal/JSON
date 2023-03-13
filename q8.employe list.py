# import json
# d={}
# c=0
# for i in range(4):
#     name=input("enter name:")
#     work=input("enter work:")
#     age=int(input("enter age:"))
#     sal=int(input("enter salary:"))
#     c+=1
#     d.update({c:{"name":name,"Designation":work,"age":age,"salary":sal}})
# # print(d)
# with open("data.json","w") as r:
#     json.dump(d,r,indent=3)


import json

a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e1={}
e2={}
e3={}
e4={}
e={}
for i in range(len(a)):
    e1.update({"name":a[0],"Designation":a[1],"age":a[2],"salary":a[3]})
for j in range(len(b)):
    e2.update({"name":b[0],"Designation":b[1],"age":b[2],"salary":b[3]})
for k in range(len(c)):
    e3.update({"name":c[0],"Designation":c[1],"age":c[2],"salary":c[3]})
for l in range(len(d)):
    e4.update({"name":d[0],"Designation":d[1],"age":d[2],"salary":d[3]})
e.update({"emp1":e1,"emp2":e2,"emp3":e3,"emp4":e4})
with open("emp data.json","w") as m:
    json.dump(e,m,indent=2)
