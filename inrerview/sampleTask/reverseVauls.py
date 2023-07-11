def reverse_vowels(simple:str):
    r={}
    for index,letter in enumerate(simple):
        if letter in 'aeiou':
            r[index]=letter
    print(r)
    
    x=simple.replace('e',r[4]).replace('0',r[1])
    print(x)
        

reverse_vowels("Hello!") # "Holle!"