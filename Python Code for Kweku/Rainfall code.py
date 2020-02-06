def myf():
    rainfall= open("Rainfall.dat","r")
    outfile=open("RainfallinCm.dat","w")
    for aline in rainfall:
        values= aline.split()
        #print(values[0],"had",values[1], "inches of rain")
        inches= float(values[1])
        centi = inches * 2.54
        print(values[0] + "" + str(centi), file=outfile)
        
    rainfall.close()
    outfile.close()
myf()

