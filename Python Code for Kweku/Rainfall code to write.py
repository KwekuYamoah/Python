rainfall=open("Rainfall.dat","w")
for aline in rainfall:
    values = aline.split()
    centi= float(values[1]) * 2.54
rainfall.close()
