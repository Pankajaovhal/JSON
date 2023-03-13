import json

d={"Name":"Abhishek",
    "Designation":"CEO of navgurukul",
    "Gender":"male",
    "Age":"29"
    }
with open("Json_file.json","w")as f:
    json.dump(d,f,indent=3)
