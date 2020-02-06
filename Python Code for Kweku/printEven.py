#A program to print out the even integrs in a given list
# Author: Kweku Yamoah

def e_print():
    num_list = input("Enter your list of numbers seprated by a comma:\n")
    int2_string = []
    list = num_list.split(",")
    int_string=[]
    for i in list:
        if int(i) % 2 == 0:
            int_string.append(i)
    print(int_string)
    
e_print()
  



    
