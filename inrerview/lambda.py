
lst1=[10, 20, 30, 40, 50, 60]

double_nums=map(lambda num: num * 2,lst1)
print(list(double_nums))

lst1=["Jane", "Lee", "Will", "Brie"]
val=map(lambda str:"hellow "+str,lst1)
print(list(val))

lst11=[100, 200, 300, 400, 500]
lst12=[1,10,100,1000,10000]
negative=[1,-10,-100,1000,10000]
lst3 = list(map(lambda x,y: x+y, lst11, lst12))
print(lst3)

x=list(filter(lambda x:x>0,negative))
print(x)
str1="Winter Olympics in 2022 will take place in Beijing China"
lst = list(filter(lambda x: True if x.lower() in "aeiou" else False, str1))