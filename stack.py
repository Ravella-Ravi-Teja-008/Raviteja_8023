print("8023,Raviteja")

a=[]
b=int(input("size of the stack: "))
c=int(input("To continue press 1 else press 0 : "))

while c!=0:
    d=int(input("To push press 1 and press 0 to pop : "))
    if d==1:
        if len(a)<=b:
            a=a+[input("Enter an element: ")]
            print("Current Stack is: ",a)
        else:
            print("Stack Overflow situation")
    elif d==0:
        if len(a)>0:
            print(a.pop())
            print("Current Stack is: ",a)
        else:
            print("Stack Underflow situation")

    c=int(input("To continue press 1 else press 0 to exit: "))

