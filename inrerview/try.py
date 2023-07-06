# def func1(*args):
#     for i in args:
#         print(i)
# func1(20, 40, 60)
# func1(80, 100)


# def calculation(a, b):
#     return a + b, a - b

# # get result in tuple format
# # unpack tuple
# add, sub = calculation(40, 10)
# print(add, sub)

# def show_employee(name,salary=9000):
#     print(f"Name: {name} salary: {salary}")

# show_employee("Ben", 12000)
# show_employee("Jessa")

# def outer_fun(a, b):
#     square = a ** 2

#     # inner function
#     def addition(a, b):
#         return a + b

#     # call inner function from outer function
#     add = addition(a, b)
#     # add 5 to the result
#     return add + 5

# result = outer_fun(5, 10)
# print(result)

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
show_student=display_student
show_student("Emma", 30)

# def evenNumbers(num):
#     d=[]
#     for x in range(1,num):
#         if x % 2 ==0:
#             d.append(x)
#     return d
        
# print(evenNumbers(30)) 

# def evenNumbers(n):
#     return[num for num in range(4,n) if num % 2 ==0] 
  
# print(evenNumbers(30))
# print(list(range(4, 30, 2)))

def largeItemInList(d):
    print(max(d))

x = [4, 6, 8, 24, 12, 2]
largeItemInList(x)


def maxVal(someList):
 max_val=someList[0]
 idx=0
 for i in range(len(someList)):
    if someList[i]>max_val:
       max_val=someList[i]
       idx =i
 print(max_val,idx)

x = [4, 6, 8, 24, 12, 2]
maxVal(x)

# def reversList(somelist:list):
#    x=somelist
#    print(somelist)
#    print(somelist[::-1])
#    print(list(reversed(somelist)))
# #    print(x.reverse())

   

# list1 = [100, 200, 300, 400, 500]
# # list1.reverse()
# reversList(list1)


# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# ['My', 'name', 'is', 'Kelly']

# result = [i + j for i, j in zip(list1, list2)]
# print(list(result))

numbers = [1, 2, 3, 4, 5, 6, 7]

odds=[num*num for num in numbers]
print(odds)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)

list3 = [10, 20, 30, 40]
list4 = [100, 200, 300, 400]
for x, y in zip(list3, list4[::-1]):
    print(x, y)

list5 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

empty=[char for char in list5 if char not in ""]
print(empty)
res = list(filter(None, list5))
print(res)


def addNewItem(someList:list,value,newvalue):
   print (someList.index(newvalue))
#    someList.append(value)
#    print(someList)
#    print(value in someList)
   

list9 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
val=7000
newVal=10
addNewItem(list9,val,newVal)

def swapLatInFirst(ls:list):
   first=ls[0]
   last=ls[len(ls)-1]
   ls[0]=last
   ls[len(ls)-1]=first
   print(ls)
vae=[12, 35, 9, 56, 24]

swapLatInFirst(vae)

def swapList(newList):
    size = len(newList)
     
    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList

def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList

def swapList(list):
     
    start, *middle, end = list
    list = [end, *middle, start]
     
    return list
     
# Driver code
newList = [12, 35, 9, 56, 24]



# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

def multyp():
   sd=[]
   for num in range(2000,3200):
      if num % 7 == 0 and num % 5 ==0:
         sd.append(num)
   print(sd)

def abs(num:numbers)->numbers:
   if num <=0 or isinstance(num, float):
      return num * -1


      
    