import time
def feboIter(n):
    prevNum=0
    currentNum=1
    for i in range(1,n):
        preprenum=prevNum
        prevNum=currentNum
        currentNum=prevNum+preprenum
    return currentNum    


def feboRecur(n):
     if n==0:
         return 0
     if (n==1):
         return 1
     else:
         return feboRecur(n-1)+feboRecur(n-1)
if __name__=="__main__":
    num=int(input("enter the number")) 
    init=time.time()
    print(f"using recursions value of fib ({num}) is a {feboRecur,{num}}")    
    print(f"using recursions value of fib ({num}) is a {feboIter,{num}}") 
    print(f"it took {time.time()-init} second")   