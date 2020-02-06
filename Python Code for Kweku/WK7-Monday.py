def func():
    word= input("Enter your ideal word:\n")
    return word
    
    
def drome():
    word=func()
    wordr = word[::-1]
    if word == wordr:
        print(" Your " + word + " is a palindrome")
    else:
        
        print("This " + word + " is not a palindrome")
        drome()
        
       
                
#drome()


    
    

from math import sqrt
def quad_effi(a,b,c):
    d= (b**2) - (4*a*c)
    quad1= (-b +sqrt(d))/2*a
    return quad1
def quad1_effi(a,b,c):
    d= (b**2) - (4*a*c)
    quad2= (-b-sqrt(d))/2*a
    return quad2
def main():
    a = int(input("Enter the cofficients of x**2:\n"))
    b = int(input("Enter the cofficients of x:\n"))
    c= int(input("Enter the c\n"))
    print("Your roots are",round(quad_effi(a,b,c)),"and",round(quad1_effi(a,b,c)))
main()
    

    
    
    