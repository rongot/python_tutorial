
# for loop for example
numbers=[1,2,3]
double_numbers=[]
for num in numbers:
    double_nums=num*10
    double_numbers.append(double_nums)
print(double_numbers)
###################################################
nums1=[1,2,3]
print([x*10 for x in nums1])
str_list=[str(num) for num in nums1]
print(str_list)
###################################################

name="ronen"
friends=["aba","saba","daba"]
x=[char.upper() for char in name]
print(x)
s=[friend[0].upper()+friend[1:] for friend in friends]
print(s)

