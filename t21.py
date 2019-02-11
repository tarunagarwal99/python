s=float(input("enter your salary:"))
if(s<=150000):
        print("no tax to be paid.")
elif(s>=150000 and s<=300000):
        print("10% tax to be paid.")
        s1=s-150000
        t1=(s1*10)/100
        print("tax to be paid:",t1)
elif(s>=300000 and s<=500000):
        print("20% tax to be paid.")
        s2=s-150000
        t2=(s2*20)/100
        print("tax to be paid:",t2)
elif(s>=500000):
        print("30% tax to be paid.")
        s3=s-150000
        t3=(s3*30)/100
        print("tax to be paid:",t3)
