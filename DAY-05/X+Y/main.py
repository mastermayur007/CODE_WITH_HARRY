def transfrom(b):
    for i in range(len(b)-1):
        if b[i]=='1':
            b[i]='0'
            if b[i+1]=='0':
                b[i+1]='1'
            else:
                b[i+1]='1'
    return b
if __name__=="__main__":
    a=list("11111000001111100000")
    print(a)
    while a !=transfrom(a.copy()):
          a=transfrom(a.copy())
    print(a)                       