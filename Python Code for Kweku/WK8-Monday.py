def main():
    n = int(input("how many dou you have:\n"))
    total=0.0
    for i in range(n):
        x=float(input("Enter a number:\n"))
        total += x
        print("\n The to total is", total)
    print("\n the average of the numbers is" , total/n)
    
#main()
    
    
def main():
    i=0
    while i != 20:
        print(i)
        i+=1
#main()
        
        
'''myfile = open("WK8-Monday.txt","r")
total=0
count = 0
for lines in myfile:
    line = lines.split(",")
    for i in line:
        total += float(i)
        count += 1
print (total)
print(count)
print(count/total)
'''

def form(n):
    from math import sqrt
    fn= (((1+sqrt(5))/2)**int(n) - ((1-sqrt(5))/2)**int(n))/sqrt(5)
    return round(fn)
    
def main():
   n= int(input("Enter your value:"))
   print(form(n))
        
main()

        
