def chaos():
    print(" A simple program to show the choatic function for 20 values")
    print("")
    x, y = eval(input(" Enter a number between 0 and 1 for x and y seperated by a comma respectively: \n"))
    n = eval(input(" How many results should I print: \n"))
    for x in range(n):
        x = 3.9 *  x * (1-x)
        
    for y in range(n):
        y = 3.9 *  y * (1-y)
        print(x, "", y, sep)
chaos()
