
def remove_vowels(text:str)->str:
    x=[t for t in text if t not in "aeiou" ]
    print(''.join(x))
    return ''.join(t for t in text if t not in "aeiou" )
    # ''.join(char for char in with_vauls if char not in "aewiou")

print(remove_vowels('apple'))  # ppl
#remove_vowels('orange') # rng
# remove_vowels('pear')   # pr

def sum_odd(numberlist:list):
    # return sum(filter(lambda score: score % 2 !=0, numberlist))
    #return (sum([num for num in numberlist if num % 2 !=0]))
    # total=0
    # for num in numberlist:
    #     if (num % 2 !=0):
    #         total=num+total
    # print(total)
    pass
# sum_odd([1,2,3,4,5])
def filter3(numberlist):
    print(list(filter(lambda score: score % 3 ==0, numberlist)))

#filter3([1,2,3,4,5])

def label(numberlist):
   std=['odd' if num % 2==0 else 'even' for num in numberlist]
   print(std)
label([1,2,3,4,5]) 

def fibi(count):
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return sum(fib)

print(fibi(3))
    
def count_fruits(fruits):
 fruit_counts = {}
 for fruit in fruits:
     if fruit in fruit_counts:
            fruit_counts[fruit] += 1
            
     else:
         fruit_counts[fruit] = 1
 return fruit_counts

        
# fruits = ['apple', 'apple', 'orange', 'apple', 'pear']
# print(count_fruits(fruits))

def total_cost(fruits):
   total=0
   for fruit in fruits:
      total+=fruit['price'] * fruit['quantity']
   print(total)
    
    

fruitsA = [
  {'name': 'apple', 'price':4, 'quantity':100},
  {'name': 'orange', 'price':5, 'quantity':100},
  {'name': 'pear', 'price':6, 'quantity':100},
]
total_cost(fruitsA)

def product(numberlist):
    total=1
    for num in numberlist:
        total *= num
    print(total)

product([1,2,3,4,5])

def hcf(a,b):
    if(isinstance(a,int) and isinstance(b,int)):
        smaller = min(a, b)
    
    # Initialize the HCF as 1
    hcf = 1
    
    # Iterate from 2 to the smaller number
    for i in range(2, smaller + 1):
        # Check if i divides both a and b
        if a % i == 0 and b % i == 0:
            # Update the HCF
            hcf = i
    
    # Return the highest common factor
    print(hcf) 
    
hcf(50,100)
 
# num_list=[1,2,3,5]
# new_num_list={num:"even" if num % 2==0 else "odd" for num in num_list}
# print(new_num_list)
    