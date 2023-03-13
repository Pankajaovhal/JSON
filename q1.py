import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
with open("myfile.json", "w")as f:
  
    json.dump(dict1, f, indent = 6)
  
    f.close()
with open("myfile.json","r")as f:
    b=json.load(f)
    print(b)

# import json
# x='{"n":"p","u":"m","c":"s"}'
# y=json.loads(x)
# print(y)