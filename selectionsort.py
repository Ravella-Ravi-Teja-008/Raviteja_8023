print("Raviteja 222010308023")
arr=[]
n=int(input("enter the length of array "))
for i in range(n):
    k=int(input('enter the number '))
    arr.append(k)

count=0
for i in range(1, n):
        key = arr[i]
        j = i-1
        count+=1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key

print(arr)
print("NO. of comparisions ",count)