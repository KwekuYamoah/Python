from math import pi

def pizzaA(d):
    area = pi *(d**2/4)
    c_pinch = c / area
    return area
def pizzaC(c):
    c_pinch = c / pizzaA(d)
    return c_pinch
d=10
c= 20

print("The area of your pizza is " + str(round(pizzaA(d),2)) + " square inch")
print("The cost per square inch of your pizza is " + str(round(pizzaC(c),2)) + " cost per inch")
    
    