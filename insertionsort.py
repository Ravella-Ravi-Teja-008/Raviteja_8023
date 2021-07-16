def insertionSort(arr):
      for i in range(1, len(arr)):
          key = arr[i]
          j = i-1
          while j >= 0 and key < arr[j]:
              arr[j + 1] = arr[j]
              j -= 1
              arr[j + 1] = key


# main code
arr = []
p=int(input("enter the length of list "))
for k in range(p):
    q=int(input('enter the value: '))
    arr.append(q)
print(arr)
insertionSort(arr)
for q in range(len(arr)):
    print("% d" % arr[q])