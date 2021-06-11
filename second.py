n=int(input('enter any number'))
s=0
for k in range(1,n+1):
    if (n%k==0):
        print(k,end=" ")
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(s==n):
    print(',',n,'is a perfect number')
else:
    print(',',n,'is not a perfect number')           