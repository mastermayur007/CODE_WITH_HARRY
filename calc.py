sum=0
while True:
    UserInput=input("enter the product price :")
    if (UserInput!="q"):
        sum=sum+int(UserInput)
        print(f"order total  so far : {sum}")
    else:
        print(f"your order total sum is {sum} , thanks for shopping with us!")    
        break