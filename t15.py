a=int(input("enter your age:"))
if(a<18):
        print("not elligible for vote")
        diff=18-a
        print("can vote after",diff)
else:
        print("elligible")
