
nums=[1,2,3,4,5]
odds=[num for num in nums if num % 2 ==0]
evens=[num for num in nums if num % 2 !=0]
print(odds)
print(evens)

std=[num *2 if num % 2 == 0 else num/2 for num in nums]
print(std)

# remove vaulse
with_vauls="this is much fun"
without_vauls=''.join(char for char in with_vauls if char not in "aewiou")
print(without_vauls)

#
