def sevenBom(num:int):
    for x in range(1,num+1):
        if x % 7==0 or "7" in str(x):
            print("bom")
        else:
            print(x)
sevenBom(27)