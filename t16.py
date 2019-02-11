n=input("enter the enumber:")
length=len(n)
org=int(n)
sum=0
n1=int(n)
while(n1!=0):
        rem=n1%10
        sum+=(rem**length)
        n1=n1//10
if(sum==org):
        print("it is a armstrong number")
else:
        print("it is not an armstrong number")
