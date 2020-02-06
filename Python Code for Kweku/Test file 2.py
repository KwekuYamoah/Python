'''def main():    
    def wind_chill(temp, wind_speed):
        return 35.74 + (0.6215 * temp) - 35.75 * (wind_speed ** 0.16) \
            + 0.4275 * temp * (wind_speed ** 0.16)

    heading = ''
    for temp in range(-20, 70, 10):
        heading += "T={0:3}".format(temp)
    print("  "+heading + "  " + "\n   " + "-" * 70)   
    for wind_speed in range (0, 35, 5):
        output_line = "{:>2d}".format(wind_speed)
        for temp in range(-20, 70, 10):
            output_line += "{:>7.1f}".format(wind_chill(temp, wind_speed))
        print (output_line)
main()'''

'''import string
s1 =[2,1,4,3]
s2= ["c","a","b"]

print(s1 + s2)
print(3*s1 + 2*s2)
print(s1[1])
print(s1[1:3])


s1.remove(2)
s1.sort()
s1.append([s2.index("b")])
s2.pop(s1.pop(2))
print(s1)'''


def doc_day():
        p_doc= input("Enter name of doctor:\n")
        p_day = input("Enter day:\n")
        infile = open("Doctor file.txt", "r")
        for line in infile:
            line = line.rstrip("\n")
            doc, l_days = line.split(",[")
            
            days = eval(l_days)
            if p_doc == doc:
                for check_day in days:
                    if check_day == p_day:
                        return doc, check_day
                        
#doc_day()



def display_slots():
    option = """ 1. 13:00  2. 13:30  3. 14:00  4. 14:30  5. 15:00  6. 15:30
                 7.  16:00  8. 16:30"""
    print(option)
# This function writes an appointment to a file   
def doc_chosen():
    doc, day = doc_day()
    print(doc, day)
    display_slots()
    infile = open("Doc_chosen.txt","r")
    slot = ['13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30']
    option = int(input("Choose a slot:\n"))
    temp = infile.readlines()
    infile.close()
    newfile = open('Doc_chosen.txt', 'a')
    found = False
    for i in temp:
        i = i.rstrip()
        k = i.split(",")
        if k[0] == doc and k[1] == day and k[2] == slot[option - 1 ]:
            print("This nigger is already booked")
            found = True
            break
    if found == False:
        print(doc + "," + day + "," + slot[option - 1], file = newfile)
            
    infile.close()
    
   
    
    
#doc_chosen()

def del_appointment():
        display_slots()
        doc = input("Enter doctor booked:\n")
        day = input("Enter the appointment day:\n")
        time = input("Enter the time:\n")
        
        infile = open("Doc_chosen.txt","r")
        lines = infile.readlines()
        outfile = open("Doc_chosen.txt","w")
        found = False
        for line in lines:
            f_doc,f_day,f_time= line.split(",")
            f_time = f_time.rstrip("\n")

            if doc != f_doc and day != f_day and time != f_time :
                print("\n")
                print(doc, day, time)
                outfile.write(line)
            else:
                found = True
                
                
      
        if found == False:
            print("Yo!, gee nor come book for here")
        infile.close()
        outfile.close()
           
del_appointment()
            
                            
                            
            
                
            
    



'''print(doc_day())

def main():
    patient_time = input("Enter your time for the appointment in the 24 hr format, example 00:00:\n")
    slot= ["09:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:30","14:00",
           "14:30","15:00","15:30","16:00","16:30","17:00"]
    infile = open("Slots.txt","r")
    time = infile.readlines()
    infile = open("Slots.txt","w")
    for slot in time:
        if slot.strip('\n') != patient_time:
            infile.write(slot)
                
        
main()'''
    