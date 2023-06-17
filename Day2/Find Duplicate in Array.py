

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    # arr.sort()
    # for i in range(n-1):
    #     if arr[i]==arr[i+1]:
    #         return arr[i]
    slow,fast=0,0
    while True:
        slow=arr[slow]
        fast=arr[arr[fast]]
        if slow==fast:
            break
    
    slow2=0
    while True:
        slow=arr[slow]
        slow2=arr[slow2]
        if slow==slow2:
            return slow

    return int(slow)



    
