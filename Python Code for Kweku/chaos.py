# A program based on the chaos function but modified to ask user the number of values to print
def chaos():
    print(" This program shows a modified version of the chaos function")
    var_1= eval(input("Enter a number between 0 and 1: \n"))
    var_2 = int(input("Enter the number of values to print: \n"))
    for a in range(var_2):
        var_1= 3.9 * var_1 * (1-var_1) #var_1 shows the chaotic function which keeps on updating in the range
        print(str(var_1))
chaos()
                
