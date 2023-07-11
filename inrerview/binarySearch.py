# function take two params list and target param
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binarySearch(simpleList:list,target):
    # if target in simpleList:
        middle=0
        start=0
        end=len(simpleList)
        steps=0
        while start <= end:
            print(f"steps:{steps} :{str(simpleList[start:end+1])}")
            steps+=1
            middle=(start+end) // 2
            # start +=1
            if target == simpleList[middle]:
                return middle
            if target<simpleList[middle]:
                end=middle-1
            else:
                 start=middle+1
        return -1
        # mid=len(simpleList)//2
        # print(simpleList[mid])

first_list=list(range(1,11))
binarySearch(first_list,7)

def binarySearch1(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1


