a=[]
p=int(input('enter no. of values'))
for k in range(p):
    e=int(input('enter the number'))
    a.append(e)


n=len(a)
for i in range(n-1):
    flag=0

    for j in range(n-1):
        if a[j]>a[j+1]:
            emp=a[j]
            a[j]=a[j+1]
            flag=1

    if flag==0:
        break
print(a)
    
