import json

a='{"s":4,"b":"3+3j","c":6}'
d=json.loads(a)
for i in d:
    if type(d[i])==str:
        d[i]=complex(d[i])
        print(d[i],", yes")
    