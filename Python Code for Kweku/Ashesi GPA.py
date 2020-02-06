# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 08:25:30 2019

@author: Kweku Yamoah
"""

def main():
    num = str(input("Enter a number:\n"))
    total = 0
    count = 0
    while num != " ":
        convert_num =int(num)
        total += convert_num
        count =  count + 1
        num = str(input("Enter a number,(hit sapce to exit if no numbers are there again):\n"))
    
    print("The average of your inputs is :" + str(round(total/count,4)))
    
#main()
    

def main(): #defining a function called main
    total = 0
    for i in range(1,6): #Decision
        total = total + int(i) #Process
        print(i) #Output for i, to show the current position of i in the loop 
        print("Temp Total is: " + str(total))  #Output, to show how the total is calculated
        
    print("Total is: " + str(total)) #final output

main() #Calling the function main to execute block of code