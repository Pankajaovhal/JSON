# import json

# d={
#     "shopping_list":
#         { 
#             "chaco":15,
#             "Biscuits":50,
#             "Diary_milk":30,
#             "ice_cream":20,
#         } 
# }
# # with open("shopping_list.json","w") as e:
# #     json.dump(d,e,indent=2)
# for i in d:
#     n=input("what do u like to buy:")
#     if type(d[i])==dict:
#         for j in d[i]:
#             if n==j:
#                 h=int(input("how much items do u want:"))
#                 d[i][j]=d[i][j]-h
# with open("shopping_list.json","w") as e:
#     json.dump(d,e,indent=2)
# e.close()


a=["123","456","678"]
#o/p:[6,15,21]

b=[]
i=0
c=int(a[i])
while i<len(a):
    
    sum=0
    j=0
    while j<len(a[i]):
        sum
        c=c+1       
        # b.append(a[i][j])
        j+=1
    i+=1
print(b)
print(c)