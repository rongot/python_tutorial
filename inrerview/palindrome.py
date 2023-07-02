def palindrome(word:str):
    mid = (len(word)-1)//2   #you can remove the -1 or you add <= sign in line 21 
    start = 0                #so that you can compare the middle elements also.
    last = len(word)-1
    flag = 0
    print(mid,last)

    while(start <= mid):
        if(word[start]==word[last]):
            print(word[start],word[last])
            start += 1
            last -= 1
        else:
            flag=1
            break

    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")


def palindrome_Or_symmetric(word:str):
    half = int(len(word) / 2)
    first_str = word[:half]
    second_str = word[half:]
    # symmetric
    if first_str == second_str:
        print(word, 'string is symmetrical')
    else:
        print(word, 'string is not symmetrical')
 
    # palindrome
    if first_str == second_str[::-1]:  # ''.join(reversed(second_str)) [slower]
        print(word, 'string is palindrome')
    else:
        print(word, 'string is not palindrome') 
  
palindrome("amaama")
palindrome_Or_symmetric("amaama")