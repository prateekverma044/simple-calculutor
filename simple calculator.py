a=int(input("enter first number"))
b=int(input("enter second number"))
choice=input("enter your choice+,-,*,/")
if choice=="+":
    print(a+b)
elif choice=="-":
    print(a-b)
elif choice=="*":
    print(a*b)
elif choice=="/":
    print(a/b)
else:
    print("invalid choice")
