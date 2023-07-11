thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])
print(len(thisdict))
thisdict["ronen"]=1
print(thisdict)
x = thisdict.get("model")
print(f"x = {x}")
y = thisdict.keys()
print(y)
z = thisdict.values()
print(z)
print(f"items={thisdict.items()}")

thisdict.update({"ronen": "cool"})
print(f"items={thisdict.items()}")

thisdict.pop("model")
print(f"items={thisdict.items()}")
