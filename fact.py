# factorial  
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def FactorialFTrialingNumber(n):
    fac=factorial(n)
    print(fac)
    count=0 
    while (fac%10==0):
        count=count+1
        fac=fac/10
    return count
if __name__ == "__main__": 
    n = int(input("Enter a number: "))
    fac=factorial(n)
    print(f"Factorial of {n} is {fac}")  
    print(f"Trailing number of {n} is {FactorialFTrialingNumber(n)}")
# Output:       
# Enter a number: 5
# Factorial of 5 is 120
# 120