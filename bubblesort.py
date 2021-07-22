print("Raviteja 222010308023")
a=[]
p=int(input('enter no. of values '))
for k in range(p):
    e=int(input('enter the number '))
    a.append(e)


count=0
for i in range(p-1):
    flag=0

    for j in range(p-1):
        count+=1
        if a[j]>a[j+1]:
            emp=a[j]
            a[j]=a[j+1]
            a[j+1]=emp
            flag=1

    if flag==0:
        break
print(a)
print("NO. of comparision ",count)
    
