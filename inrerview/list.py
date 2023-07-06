def findinlst(lst, val):
    for x in range(0,len(lst)):
        if val in lst[x]:
            print([x,lst[x].index(val)])


nested_lst=[[1,2,3], [4,5,6], [7,8,9]]
nested_lst1 = [["Hat", "Glove", "Goggle"], ["Button", "Zipper", "Hook"]]

for x in range(0,len(nested_lst1)):
    for val in nested_lst1[x]:
        if "G" in val:
            print(val,x)

# result = [item for row in nested_lst1 for item in row]
        
# findinlst(nested_lst1,'z')

# for x in range(0,len(nested_lst1)):
#     res=[y for y in nested_lst1[x]]
#     print(res)

# s=[friend for friend in nested_lst1[0] if "G" in friend]
# print(s)
# print(nested_lst.count(5))
# print(len(nested_lst))

# result = [item for row in prices for item in row]
