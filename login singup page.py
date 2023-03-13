# import json
# a={}
# b={}
# n=input("do you want to login or singin:")
# if n=="singin":
#     c=input("enter name:")
#     p=input("enter password:")
#     p2=input("conform password:")
#     if p>"a" or p<"z" and p>"A" or p<"Z" and p.isdigit():
#         if len(p)>=6:
#             if p2==p:
#                 b["name"]=c
#                 b["password"]=p
#                 b["conformed password"]=p2
#                 d=input("enter discription:")
#                 e=input("enter DOB:")
#                 f=input("gender:")
#                 a["discription"]=d
#                 a["DOB"]=e
#                 a["gender"]=f
#                 b.update(a)
#                 with open("singin.json","w") as g:
#                     json.dump(b,g,indent=2)
#             else:
#                 print("your password is incorrect try again!")
#         else:
#             print("create password more than 6digits.")
#     else:
#         print("make yor password strong.")
# else:
#     q=input("enter name:")
#     r=input("enter password:")
#     # s=input("conform password:")
#     # if s==r:
#     b["name"]=q
#     b["password"]=r
#     print("your login is successful:)")
    

# a=["121","234","456"]
# i=0
# c=[]
# while i<len(a):
#     b=int(a[i])
#     s=0
#     j=0
#     while j<len(a[i]):
#         r=b%10
#         b=b//10
#         s+=r
#         j+=1
#     c.append(s)
#     i+=1
# print(c)
# # print(s)