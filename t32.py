a=input("enter name:")
print(a.upper())
print(a.lower())
for x in range (0,len(a)):
        if(x%2==0):
                print(a[x].upper(),end='')
        else:
                print(a[x].lower(),end='')
print(a.title())
