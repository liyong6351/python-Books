import json

numbers=[1,2,3,4,5,6,7,8,9]
numbers1=[]
filename = 'number.json'

with open(filename,"w") as f:
    json.dump(numbers,f)

with open(filename,"r") as f:
    numbers1 = json.load(f)
print(numbers1)