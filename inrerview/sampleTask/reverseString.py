def reverse_string(simpleStr:str):
    print(simpleStr[::-1])
    # implement your function here
   
# reverse_string('awesome')

def list_check(simpleList:list):
    x=all(map(lambda x:type(x)is list,simpleList))
    print(x)

# list_check([[],[1],[2,3], (1,2)]) # False
# list_check([1, True, [],[1],[2,3]]) # False
# list_check([[],[1],[2,3]]) # True

def sum_pairs(simpleList:list,value:int):
    # x=0
    for num in range(len(simpleList)):
        for j in range(num+1, len(simpleList)):
            if simpleList[num]+simpleList[j] ==value:
                print([simpleList[num],simpleList[j]])
        break     
# sum_pairs([4,2,10,5,1], 6)

def vowel_count(simpleString:str):
   com={}
   vowels = "aeiou"
   for v in vowels:
    # print(v, simpleString.count(v))
    com[v]=simpleString.count(v)
   print(com)
    
     
vowel_count('awesomee')

'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

# counts = {i:0 for i in 'aeiouAEIOU'}
# >>> for char in sentence:
# ...   if char in counts:
# ...     counts[char] += 1
# ... 
# >>> for k,v in counts.items():
# ...   print(k, v)