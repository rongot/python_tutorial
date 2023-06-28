months=("January","February" , "March", "April", "May", "June", "July", "August","September", "October", "November", "December")
print(type(months))
print(months[0])
print(months[-1])

for month in months:
    print(month)

print(months.count("March"))
print(months.index("March"))
# i=len(months)-1
# while i>=0:
#     print(months[i])
#     i-=1