print("ente marks out of 100:")
n1=float(input("enter the marks of first subject:"))
n2=float(input("enter the marks of second subject:"))
n3=float(input("enter the marks of third subject:"))
n4=float(input("enter the marks of fourth subject:"))
ag=(n1+n2+n3+n4)/4
if(ag>=75):
        print("distinction.")
elif(ag>=60 and ag<75):
        print("1st division.")
elif(ag>=50 and ag<60):
        print("2nd division.")
elif(ag>=40 and ag<50):
        print("3rd division.")
else:
        print("fail!!")
