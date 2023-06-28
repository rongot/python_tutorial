numbers=dict(first=1,second=2,third=3)
print (numbers)
squre_number={key:value **2 for key,value in numbers.items()}
print(squre_number)

print({num:num*3 for num in [1,2,3]})

str1="ABC"
str2="123"
combo={str1[i]:str2[i] for i in range(0,len(str1))}
print(combo)

num_list=[1,2,3,5]
new_num_list={num:"even" if num % 2==0 else "odd" for num in num_list}
print(new_num_list)


user_info = {
            "name": "Blue",
            "age": "10",
            "email": "blue@gmail.com"
            } 

new_user_info={(k.upper() if k is "name" else k ):v.upper() for k,v in user_info.items()}
print(new_user_info)


