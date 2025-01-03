a=int(input("enter the first number:"))
b=int(input("enter the second number:"))

maxnum=max(a,b)
while (True):
    if (maxnum%a==0 and maxnum%b==0):
        print("LCM is:",maxnum)
        break
    else:
        maxnum+=1
        