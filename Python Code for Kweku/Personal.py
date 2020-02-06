#Displaying name and address just like it is formatted on an envelope

print("Kweku Andoh Yamoah")
print("Computer Science '22")
print("P.O. Box Ml-401")
print("When there is a will there is a way")

print()

def main():
    index= input("Enter your numbers seperated by a comma:\n")
    index1=[]
    for i in index.split():
        index2= eval(i)
        index1.append(chr(index2))
    message= "".join(index1)
    print(message)


def happy():
    name = input("Enter your name:\n")
    print("Hello" + "" + name)


def area():
    len1= float(input("Enter your length in centimeters\n"))
    wid2= float(input("Enter your width in centimeters\n"))
    area= len1 * wid2
    print("The area of your farm is " + " " + str(area) + " centimeters")
#area()

def refund():
    less= 0.10
    more = 0.25
    less1= int(input("How many containers of a litre or less do you have:\n"))
    more1= int(input("How many containers above a litre do you have:\n"))
    refund = less * less1 + more * more1
    print("Your refund is $",round((refund),2))
    
#refund()
    

def taxOwed(meal_cost):
    tax = 0.1 * meal_cost
    return tax
def tipAmt(meal_cost):
    tip = 0.18 * meal_cost
    return tip
def main():
    meal_orderc = float(input("Enter the cost of the meal you ordered:\n"))
    grandtotal= taxOwed(meal_orderc) + tipAmt(meal_orderc) + meal_orderc
    print("Your taxed amount is $",round(taxOwed(meal_orderc),2))
    print()
    print("Your expected tip amount is $",round(tipAmt(meal_orderc),2))
    print()
    print("You are to pay $", round((grandtotal),2))
#main()
    
    
def prod(widget,gizmos):
    order = 0.075 * widget + (0.112 * gizmos)
    return order
def main():
    w= eval(input("Enter the number of widgets bought\n:"))
    g= eval(input("Enter the number of gizmos bought:\n"))
    print("Your order is ", round(prod(w,g),2), " kg")
    
#main()
          
          
def main():
    principal= eval(input("Enter the amount you deposited into the account:\n"))
    compI=0
    for i in range(1,4):
        compI= (principal*4*i)/100
        compI += compI + principal
        print(round(compI,2))
    print("Thanks for using the service")
    
#main()
from math import *
def main():
    a,b=eval(input("Enter the values of a and b seprated by commas:\n"))
    print("The sum of a and b is"," ",a + b)
    print("the difference of a and b is"," ", b-a)
    print("The product of a and b is "," ", a *b)
    print("the quotient is"," ", a / b)
    print("The remainder of a and b is"," ", b % a)
    print("The logarithim of a is"," ", log10(a))
    print("The exponeation of a and b is"," ", a ** b)

#main()


from math import pi
def volarea(radius):
    area = pi * radius ** 2
    volume = 4/3 * pi * radius ** 3
    return area, volume

def main():
    r = int(input("Enter the radius of your circle:\n"))
    print("The area and volume of your circle is", volarea(r), "respectively")
#main()
    
    
    