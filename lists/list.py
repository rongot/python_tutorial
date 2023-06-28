tasks=["ronen","gotliv"]
print(len(tasks))

n=range(1,10)
print(type(n))
r=list(range(1,10))
# r=list(r)
print(r)
# check if value in a list
# value in list
# names=["ronen","gotliv","moshe"]
# print("ronen" in names)
# iterate over lists

# for num in r:
#     print(num) 

# for index, item in enumerate(r):
#     print(index, item)

# index=0
# while index<len(r):
#     print(index,r[index])
#     index +=1

# list method
# appemd add item to the end of list
r=list(range(1,8,2))
print(r)
r.append(12)
print(r)
# extend add to the end of list all values passed to extend
r=list(range(1,8,2))
print(r)
r.extend([20,30,40])
print(r)
# insert insert an item at a given position
first_list=list(range(1,8,2))
first_list.insert(2,"hi")
first_list.insert(-1,"bye")
print(first_list)
#  clear
first_list.clear()
# pop remove item at a given position in the list, return it 
# if not index is specified ,removes & return last item in the list
first_list=list(range(1,8,2))
print(first_list.pop())
print(first_list.pop(1))
# remove :removes the first item from the list whosw values is x
#throw ValueError if item is not found

# index
index_list=[5,5,6,7,9,5,4]
print(index_list.index(5))# 0
#can specify start and end index
print(index_list.index(5,1))# 1
print(index_list.index(5,2))# 5
print(index_list.index(5,2,6))# 5

# join

names=["mr","ronen"]
print('.'.join(names))
words=["code","is","fun"]
print(' '.join(words))

# slice

slice_list=[1,2,3,6]
print(slice_list[1:]) #[2, 3, 6]

