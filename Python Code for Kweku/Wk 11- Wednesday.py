def main():
    printIntro()
    n = getInput()
    coord()
    pi= simNThrows(n)
    printSum(n,pi)
    
def printIntro():
    print("This is a program that simulates the value of pi, \n using a dartboard game \n")
    print("n is the number of games you would like to simulate\n")
    print("h is the number of darts thrown that hit the board \n")
    print("Pi is approximately calculated as 4(h/n) \n")
    
    
def getInput():
    u = int(input(" Enter the number of games you would want to simulate:\n"))
    return u

from random import random
def coord():
    x = 2 * random() - 1
    y= 2 * random() - 1
    ans = x ** 2 + y ** 2
    if ans <= 1:
        return True
    else:
        return False
    
def simNThrows(n):
    h= 0
    for i in range(n):
        coord()
        if coord():
                h += 1
    pi = 4 * ( h /n)
            
    return pi
    
def printSum(n, pi):
    n = getInput()
    print("\n Simulatted throws:",n)
    print("The approximate value of pi is {0:0.6f}".format(pi))
    
    
main()
    