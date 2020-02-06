def accum():
    rate = eval(input(" Enter yearly rate:\n"))
    no = int(input("Enter the number of times you pay in a year: \n"))
    for i in range(1,10,1):
        periodI= no * i
        accrue = rate/periodI
        print(accrue)
accum()
