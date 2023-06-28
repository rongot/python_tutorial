user_info = {
            "name": "Blue",
            "age": 10,
            "email": "blue@gmail.com"
            } 
# print(user_info["name"])

for val in user_info.values():
    print(val)
for key in user_info.keys():
    print(key)
for item in user_info.items():
    print(item)
for k,v in user_info.items():
    print(f"key {k}, value {v}")
print ("age" in user_info)
print (10 in user_info.values())
# fromkeys
newDict={}.fromkeys("a","b")
print(newDict)
newDict1={}.fromkeys(["email","username"],'unknown')
print(newDict1)
# get
print(user_info.get("a"))
print(user_info.get("name"))
# pop
clone=user_info
print(clone.pop("name"))
print(clone)

second={"city":"antigoa"}
second.update(user_info)
# user_info.update()
print(second)