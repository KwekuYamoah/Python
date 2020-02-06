def happy():
    print("Happy Birthday to You.....")
def sing(person):
    happy()
    happy()
    print("Happy Birthday to dear ", person + ".")
    happy()
def main():
    sing("Fred")
    print()
    sing("Esi")
    print()
    sing("Kweku")
#main()
    
def square(x):
    return x**2

def happy2():
    return "Happy birthday to you ! \n"
def p_verse(person):
    verse= happy2() *2  + "Happy birthday dear" + person + ".\n" + happy2()
    return verse
def main():
    outfile = open("Happy Birthday.txt","w")
    for person in ["Kweku","Esi","John"]:
        print(p_verse(person), file=outfile)
    outfile.close()
main()
    