# A program to print out the sum of the first n natural numbers
# And the sum of the cubes of the first n natural numbers.
def sumN(n):
    sum = n/2*(2 +(n-1))
    return sum
def sumNCubes(n):
    cubesum =  n/2*(2 +(n-1)) ** 2
    return cubesum
def main():
    number = int(input("Enter your natural number:\n"))
    outfile = open("sum.txt", "w")
    print("The sum of the first n natural numbers is:", sumN(number), file = outfile)
    print("The sum of the cubes of the first n natural numbers is:", sumNCubes(number), file = outfile)
    
#main()
    
def main():
    message= input("Enter the message you want to encode:\n")
    for ch in message:
        coded= ord(ch)
    print(coded,end="")
#main()
    
def main():
    code_num= input("Enter your ordinal numbers seperated by a comma:\n")
    message= []
    for i in code_num.split(","):
        new= int(i)
        word=chr(new)
        message.append(word)
    new_message= "".join(message, " ")
    print(new_message)
main()