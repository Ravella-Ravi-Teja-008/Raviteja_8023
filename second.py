n=input('enter any thing: ')
b=[]
for i in n:
    b.append(ord(i)) 

c=[]
for k in b:
    c.append(chr(k+3))
str1=''
for m in c:
    str1+=m
print('encrypted:',str1)
d=[]
for i in n:
    d.append(ord(i))
e=[]
for l in d:
    e.append(chr(l))
str2=''
for g in e:
    str2+=g
print('decrypted:',str2)     