def euclid():
     m, n = eval(input("Enter the two numbers seperated by a comma:"))
     while m != 0:
        temp = n
        n = m
        m =  temp % m
     print(n)
    
            
    
euclid() 