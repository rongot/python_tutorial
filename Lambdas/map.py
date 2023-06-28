
''' 
map a standard function that accept at least two arguments , a function and an "iterable"
iterable= something you can iterate over(list.strings,tuple sets,dictinery)
runs the lambda for each value in the iterable and returns map object which can be converted
into another data structore 


'''
nums=[1,2,3,4]
double_nums=map(lambda num: num * 2,nums)
print(list(double_nums))

people=["ronen","gotlov","moshe"]
peeps=list(map(lambda name:name.upper(),people))
print(peeps)

names=[
    {
        "firstName":"ronen",
        "lastName":"gotliv"
    },
    {
        "firstName":"moshe",
        "lastName":"fone"
    }
]


# print(names)
# print(names["firstName"])
first_names= map(lambda x: x['firstName'],names)
print(list(first_names))


l=[
 {'value': 'apple', 'blah': 2}, 
 {'value': 'banana', 'blah': 3} , 
 {'value': 'cars', 'blah': 4}
 ]
l_map=map(lambda d: d['value'], l)
print(list(l_map))


