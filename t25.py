num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
for i in range (num1,num2+1):
        print(i)
        if(i%2==0):
                print("even")
        else:
                print("odd")
