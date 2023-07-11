def titleize(words:str):
#    without_vauls=' '.join(word[0].capitalize() for word in words)
     x=words.split(" ")
     without_vauls=' '.join(word[0].capitalize()+word[1:] for word in x)
     print(without_vauls)
# titleize('this is awesome') # "This Is Awesome"

def find_factors(num:int):
    su=[]
    for n in range(1,num+1):
         if num % n ==0:
              su.append(n)
    print(su)
              

# find_factors(111) # [1,2,5,10 ]

def includes(item,val,start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]
# print(includes([1, 2, 3], 1))# True 
# print(includes('abcd', 'e')) # False
# print(includes({ 'a': 1, 'b': 2 }, 1)) # True

def truncate(string, n):
        if (n < 3):
            print("Truncation must be at least 3 characters.") 
        if (n > len(string) + 2):
            print(string) 
 
        print(string[:n - 3] + "...") 


truncate("Hello World", 6)# "Hel..."

# def two_list_dictionary(test_keys:list,test_values:list):
    
#     if len(test_keys) == len(test_values):
#          res = dict(zip(test_keys, test_values))
#          print(res)
#     if len(test_keys) > len(test_values):
#     #    newdict={key:value for key in ls for value in ls1}
#          res = dict(zip(test_keys, test_values))
#          print(res)
#     if len(test_keys) < len(test_values):
#          print("c")
#          print(len(test_keys),len(test_values))

def two_list_dictionary(keys, values):
    collection = {}
 
    for idx, val in enumerate(keys):
        if idx < len(values):
            collection[keys[idx]] = values[idx]
            # print(collection[keys])
        else:
            collection[keys[idx]] = None
 
    return collection

# print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3,4])) # {'a': 1, 'b': 2, 'c': 3, 'd': None}

def range_in_list(simplelist:list,start:int,end:int)->int:
    print(sum(simplelist[start:end]))
# range_in_list([1,2,3,4],0,2)
# range_in_list([1,2,3,4],0,100)

def same_frequency(firstFreq,second:int):
   d1 = {letter:str(firstFreq).count(letter) for letter in str(firstFreq)}
   d2 = {letter:str(second).count(letter) for letter in str(second)}
#    print(d1)
   for key,val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
   return True
# same_frequency(551122,221515)

def find_the_duplicate(arr:list):
    counter = {}
    for val in arr:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)
    

def sum_up_diagonals(arr:list):
  total=0
  for num in arr:
      for d in num:
          total +=d
#   print(total)
# list1 = [
#   [ 1, 2 ],
#   [ 3, 4 ],
#   [5,6]
# ]
 
# sum_up_diagonals(list1) # 10

def min_max_key_in_dictionary(obj:dict):
    r=[]
    for num in obj.keys():
        r.append(num)
    print([min(r),max(r)])

min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]