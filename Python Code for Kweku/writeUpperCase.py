def main():
    
    infile= open("Assignmet.txt","r")
    infileR= infile.read()
    #print(infile)
    outfile = open("Assignment_r.txt", "w")
    outUp=infileR.upper()
    outfile.write(outUp)
    outfile.close()
    infile.close()
main()
