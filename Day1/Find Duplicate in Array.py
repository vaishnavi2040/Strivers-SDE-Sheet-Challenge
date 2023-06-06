

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    arr=sorted(arr)
    n=len(arr)
    
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            return arr[i]
    pass
