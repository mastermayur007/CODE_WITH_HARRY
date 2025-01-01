SECURE = (('s', '$'), ('and', '&'), 
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'),(" ", "_"))

def sequrepassword(password):
    for a,b in SECURE:
        password=password.replace(a,b)
    return password    

if __name__=="__main__":
    password= input("Enter your password\n")
    password=sequrepassword(password)
    print(f"Your sequre password is {password}")
    