num=int(input("enter a number:"))
iscomposite=0
for i in range (2,num):
        if(num%i==0):
                iscomposite=1
                break
        if(iscomposite==1):
                print("given number is composite number",format(num))
        else:
                 
                 print("given number is prime number",format(num))
        
