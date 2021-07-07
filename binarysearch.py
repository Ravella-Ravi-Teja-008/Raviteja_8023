def binary_search(arr,low,high,x):
    if high>low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif mid>x:
            return binary_search(arr,low,mid-1,x)
        elif mid<x:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1
        

print("raviteja 222010308023")      
arr=[20,26,45,56,454,465,988,1000]
result=binary_search(arr,0,len(arr)-1,988)
if result !=-1:
    print("found",result)
else:
    print("not found")