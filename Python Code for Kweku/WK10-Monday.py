ans=input("What flavour")
if ans!= "":
    flavour= ans
else:
    flavour="vanilla"
print(flavour)



def main():
    win= GraphWin("Color Window", 500, 500) 
# Event Loop: handle key presses until user presses the "q" key.
    while True:
        key = win.getKey()
        if key== "q":
            #loop exit
            break 
#process the key
    if key == "r":
        win.setBackground("pink")
    elif key == "w" :
        win.setBackground("white")
    elif key== "g":
        win.setBackground("lightgray")
    elif key == "b":
        win.setBackground("lightblue") 
# exit program
    win. close() 
#main()
    
    
    
def windIndex(t,v):
    chill= 35.74 + 0.6215 * t- 35.75 *v ** .16+ 0.4275 *t *v** .16
    return chill


def main():
    heading = ''
    for t in range(-20, 61, 10):
        heading += "T={0:3}".format(t)
    print("  "+heading + "  " + "\n   " + "-" * 70)   
    for v in range(0,51,5):
        print("V={0:3}".format(v),end="  ")
        
        for t in range(-20,61,10):
            chill= windIndex(t,v)
            print("{0:9.2f}".format(chill),end="")
        print()
        
main()
            
       for t in range(-20,-11,10):
        print("{0:9}T={1:3}".format("",t),end="")
    for t in range(-10, 61, 10):
        print("{0:5}T={1:3}".format("",t),end="")
    print() 
