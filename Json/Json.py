import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

# convert json to dict
y = json.loads(x)

#-----------------------------------------------------

d = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#Convert any python object (dict - list - touple ...) to json
j = json.dumps(d)

# print(type(j)) --> String

#-----------------------------------------------------

myDickt = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# Format the Result
# print(json.dumps(myDickt, indent = 3, sort_keys = True))

#-----------------------------------------------------

# json File

with open('./sample4.json', 'r') as fileReader:

    # attention  --->  load 
    data = json.load(fileReader)

key = 'people'

# if key in data:
    # print(data[key])

#-----------------------------------------------------

# json array

json_array = data[key]

# for i in json_array:
#     print(i)

#-----------------------------------------------------

# save (Dump) 

List = [10, 20, 30, 696, 54]

file_path = 'numbers.json'

with open(file_path, 'w') as File:
    
    json.dump(List, File)

#-----------------------------------------------------

# Load 

file_path = 'numbers.json'

with open(file_path) as File:
    
    Detail = json.load(File)

print(Detail)