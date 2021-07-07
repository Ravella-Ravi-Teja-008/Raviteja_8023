def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
  
    return -1


print("Raviteja 222010308023")
arr=[1,252,43,34,87,45,76]
result=search(arr,87)
if result !=-1:
    print('element is found',result)
else:
    print("ele not found")