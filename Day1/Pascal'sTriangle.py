#question link- https://www.codingninjas.com/codestudio/problems/pascal-s-triangle_8230805?challengeSlug=striver-sde-challenge&leftPanelTab=0

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    ans=[]
    ans.append([1])
    
    for i in range(n-1):
        t=[0]+ans[-1]+[0]
        row=[]
        for j in range(len(ans[-1])+1):
            row.append(t[j]+t[j+1])
        ans.append(row)    
        
    return ans
