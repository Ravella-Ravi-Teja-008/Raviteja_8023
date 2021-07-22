print('Raviteja 222010308023')
arr=[]
n=int(input("enter the length of array: "))
for i in range(n):
    q=int(input('enter the element'))
    arr.append(q)

b=len(arr)
count=0
for i in range(1,b):
    j=arr[i]
    p=i
    k=i-1
    while k>=0:
        if arr[k]>j:
            arr[k],arr[p]=arr[p],arr[k]
            count+=1
            k-=1
            p-=1
        else:
            break

print(arr)
print("NO. of comparisions: ",count)