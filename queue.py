print("8023,Raviteja")

a=[]
b=int(input("size of the queue: "))
c=int(input("To continue press 1 else press 0 : "))

while c!=0:
    d=int(input("To push press 1 and press 0 to remove : "))
    if d==1:
        if len(a)<=b:
            a=a+[input("Enter an element: ")]
            print("Current queue is: ",a)
        else:
            print("queue Overflow situation")
    elif d==0:
        if len(a)>0:
            print(a.pop(0))
            print("Current queue is: ",a)
        else:
            print("queue Underflow situation")

    c=int(input("To continue press 1 else press 0 to exit: "))

