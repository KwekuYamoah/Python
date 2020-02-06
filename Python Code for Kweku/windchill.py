def windIndex(t,v):
    chill= 35.74 + 0.6215 * t- 35.75 *v ** .16+ 0.4275 *t *v** .16
    return chill


def main():
    for t in range(-20,-11,10):
        print("{:^9}".format(""),"T={0:^8}".format(t),end="")
    for t in range(-10, 61, 10):
        print("{:^2}".format(""),"T={0:^3}".format(t),end="  ")
        
    print( "\n   " + "-" * 95)
    
    for v in range(0,51,5):
        print("V={0:3}".format(v),end="  ")
        
        for t in range(-20,61,10):
            chill= windIndex(t,v)
            print("{0:10.2f}".format(chill),end="")
        print()
        
        
main()