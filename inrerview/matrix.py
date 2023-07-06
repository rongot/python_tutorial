test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]] 

# r={}.fromkeys(test_list[0],)
res = {test_list[0][ele] :  test_list[ele + 1] for ele in range(len(test_list) - 1)}
res = dict(zip(test_list[0], test_list[1:]))
thisdict = dict.fromkeys(test_list[0],test_list[1])
print(thisdict)