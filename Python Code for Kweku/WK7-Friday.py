def main():
    credit = float(input("Enter your credit:\n"))
    if credit  < 7 or credit <= 10:
        print("You are a Freshman")
    elif  credit  < 16:
        print("You are a sophomore")
    elif  credit  < 26:
        print("you are a junior")
    else:
        print("FINAL YEAR CONGRATS")

main()
        
        
        
#def main():
    #print("You can enter your time in the 24 hour format")
    #startHr= eval(input("Enter the hour you started:\n"))
    #startMin = eval(input("Enter your start min:\n"))
    #endHr = eval(input("Enter your end time:\n"))
    #endMin= eval(input("Enter your end min:\n"))
    
    #if endHr > 21 and startHr >=6:
        #if startMin > 0 and endMin > 0:
            #payment = ((endHr - 21) * 1.75) + (((12-startHr) + (21-12)) * 2.50) + ((endHr - startHr)/60 * 2.50)
    #print(payment)
        
    #else:
        #payment = ((endHr - startHr) * 2.50) + ((endHr - startHr)/60 * 2.50)
        #print(payment)
#main()