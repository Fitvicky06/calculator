def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "not divisible by zero"
    else:
        return a/b
while True:   
 print("1.ADD")
 print("2.SUBTRACT")
 print("3.MULTIPLY")
 print("4.DIVIDE")
 print("5.EXIT")

 choice=int(input("enter your choice from 1-5 :"))

 if choice==5:
    print("thank you for using")
    break

 num1=int(input("enter first number :"))
 num2=int(input("enter second number :"))

 if choice==1:
    print("result :",add(num1,num2))
 elif choice==2:
    print("result :",subtract(num1,num2))
 elif choice==3:
    print("result :",multiply(num1,num2))
 elif choice==4:
    print("result :",divide(num1,num2))
 else:
    print("invalid choice")