n=int(input("enter the number:")) #input the number
sum=0  #starting from zero
order=len(str(n))  #for get a number from the given input
copy_n=n  #for not getting less then zero
while (n>0): #the loop will run until the number is greater than zero1
    digit=n%10
    sum=sum+digit**order
    n=n//10
if (sum==copy_n):
    print(f"{copy_n} is a armstong number") 
else:
    print(f"{copy_n} is not a armstrong number")       