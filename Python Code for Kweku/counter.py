def counter():
    infile= open("Assignmet.txt","r")
    infileR= infile.readlines()
    print("The number of lines is",len(infileR))
    counter=0
    for lines in infileR:
        lines= lines.split()
        counter += len(lines)
    print("The number of words in the file is ", counter)



    infile= open("Assignmet.txt","r")
    infileR= infile.read()
    print("The number of characters in this file",len(infileR))
counter()