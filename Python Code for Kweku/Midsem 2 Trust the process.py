greet = "Hello Bob"
#print(greet)


def main():
    firstname= input("Enter your firstname:\n").lower()
    lastname = input("Enter your last name:\n").lower()
    u_name= firstname[0] + lastname[:7]
    print(u_name + "@ashesi.edu.gh")
#main()
    
def main():
    n = int(input("Enter a month number (1-12) : ")) 
    pos = (n-1)*3
    months= "JanFebMarAprMayJunJulAugSepOctNovDec"
    monthAbrv= months[pos : pos+3]
    print(monthAbrv)
#main()


def main():
    infileName= input(" What file do you want to read;\n")
    outfileName= input(" What file do you want to write to: \n")
    
    infile= open("infileName.txt","r")
    outfile= open("outfileNmae.txt","w")
    
    
    for lines in infile:
        firstname, lastname = lines.split()
        uname = (firstname[0] + lastname[:7]).lower()
    print(uname, file=outfile)
    
    infile.close()
    outfile.close()
    
#main()
    
def main():
    acronym=input("Enter the term you want to creat an acronym for:\n")
    new= acronym.split()
    real=""
    for words in new:
        real += words[0].upper()
    print(real)
#main()

def main():
    letters= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    name = input("Enter your name:\n").lower()
    realV=0
    for ler in name.split():
        for ler in ler:
            value = letters.index(ler) + 1
            realV += value
    print(str(realV))
    
#main()

for w in "Now is the winter of our discontent ... ". split() :
    print (w) 

print("Time left {0:02}:{1:05.2f}".format(1, 37.374))         
        
def main():
    n= eval(input("Enter a positive number:\n"))
    prev = 1
    fib = 1
    for i in range(2,n):
        temp = prev
        prev= fib
        fib +=temp
    print("Fib", n, "is", str(fib))
    
    
#main()

def main():
    n = eval(inpu("Enter a number:\n"))
    total=0
    while i != n:
        for i in range(n):
            total += i
    print(total)
main()
    