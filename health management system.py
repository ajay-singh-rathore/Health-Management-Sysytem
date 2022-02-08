# Health management system
def datetime():
    import datetime
    return datetime.datetime.now()

def type(k):
    if k==1:
        c=int(input("Enter 1 for exercise  Enter 2 for Diet : "))

        if c==1:
            value = str(input("Type here : "))
            with open("Harry-ex.txt","a") as op:
                op.write(str([str(datetime())])+": "+value+"\n")
            print("<----Sucessfully written---->")
        if c==2:
            value = str(input("Type here : "))
            with open("Harry-food.txt","a") as op:
                op.write(str([str(datetime())])+": "+value+"\n")
            print("<---Sucessfully Written---->")
    elif k==2:
        c=int(input("Enter 1 for exercise \n Enter 2 for Diet : "))
        if c==1:
            value = str(input("Type here : "))
            with open("Rohan-ex.txt","a") as op:
                op.write(str([str(datetime())])+": "+value+"\n")
            print("<----sucessfully written---->")
        elif c==2:
            value = str(input("Type here : "))
            with open("Rohan-food.txt","a") as op:
                op.write(str([str(datetime())])+": "+value+"\n")
            print("<----Sucessfully written---->")
    elif k==3:
        c=int(input("Enter 1 for exercise \n Enter 2 for Diet : "))
        if c==1:
            value = str(input("Type here : "))
            with open("Hammad-ex.txt","a") as op:
                op.write(str([str(datetime())])+": "+value+"\n")
            print("<----Sucessfully Written---->")
        elif c==2:
            value = str(input("Type here : "))
            with open("Hammad-food.txt","a") as op:
                op.write(str([str(datetime())])+": "+value+"\n")
    else:
        print("sorry! Invalid option : ----> ")

def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for exercise \n Enter 2 for Diet : "))
        if c==1:

            with open("Harry-ex.txt") as op:
                for i in op:
                    print(i,end=" ")
        elif c==2:

            with open("Harry-food.txt") as op:
                for i in op:
                    print(i,end=" ")
    elif k==2:
        c=int(input("Enter 1 for exercise \n Enter 2 for Diet : "))
        if c==1:
            with open("Rohan-ex.txt") as op:
                for i in op:
                    print(i,end=" ")
        elif c==2:
            with open("Rohan-food.txt") as op:
                for i in op:
                    print(i,end=" ")
    elif k==3:
        c=int(input("Enter 1 for exercise \n Enter 2 for Diet : "))
        if c==1:
            with open("Hammad-ex.txt") as op:
                for i in op:
                    print(i,end=" ")
        elif c==2:
            with open("Hammad-food.txt") as op:
                for i in op:
                    print(i,end=" ")
    else:
        print("Invalid choice")
print("<-=------------------HEALTH MANAGEMENT SYSTEM---------------------=>")
a=int(input("Press 1 for log  Press 2 for Retrieve \n"))
if a==1:
    b=int(input("Press 1 for Harry \n Press 2 for Rohan \n Press 3 for Hammad \n"))
    type(b)
else:
    b=int(input("Press 1 for Harry \n Press 2 for Rohan \n Press 3 for Hammad \n"))
    retrieve(b)






