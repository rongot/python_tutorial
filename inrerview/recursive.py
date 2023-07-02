# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

def addition(num):
    if num:
        print(type(num))
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)