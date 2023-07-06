# Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print({**dict1})


sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])

sampleDict1 = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict1[k] for k in keys}
print(newDict)

sample_dict2 = {'a': 100, 'b': 200, 'c': 300}
print(200 in sample_dict2.values())

sample_dict4 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print (f"{min(sample_dict4,key=sample_dict4.get)} {min(sample_dict4.values())}")


        