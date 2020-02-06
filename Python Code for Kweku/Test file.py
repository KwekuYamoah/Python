def elucid():
    m, n = eval(input("Enter the two numbers seperated by a comma:"))
    while m != 0:
        temp = n
        n = m
        m =  temp % m
        print(n)
    
        
            
    
#elucid()
        
        
##
#Python's program to calculate the Wind Chill Index (WCI)
#The wind chill index is only considered valid for temperatures less than or
#equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per hour.
##
 
#Define the constants
WINDCHILL_OFFSET    = 13.12
WINDCHILL_FACTOR1   = 0.6215
WINDCHILL_FACTOR2   = -11.37   
WINDCHILL_FACTOR3   = 0.3965
WINDCHILL_EXP       = 0.16
 
 
#Read the inputs from user air temperature and wind speed
#temp    = float(input("Enter the air temperature in (degrees Celsius): "))
#speed   = float(input("Enter the wind speed (kilometer per hour): "))
 
#Calculate the WCI
#wci     = WINDCHILL_OFFSET + (WINDCHILL_FACTOR1 * temp) + (WINDCHILL_FACTOR2 * speed ** WINDCHILL_EXP) + (WINDCHILL_FACTOR3 * temp * speed ** WINDCHILL_EXP)
 
#Display the result
#print("Your Wind Chill Index ","%d"%(wci))


'''def add_element(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)

d = {}
(add_element(d, 'foo', 'val1'))
add_element(d, 'foo', 'val2')
add_element(d, 'bar', 'val3')
print(d)'''


'''import random'''

'''def doc_day():
        l_days = ["Mon","Tues","Wed","Thurs","Fri"]
        infile = open("Doctor file.txt","r")
        sched={}
        r= random.randint(1,len(l_days))
        line =""
        for day in l_days:
            w = l_days[r-3]
        for doc in infile.readline():
            line += doc
            
        if line not in sched:
            sched[line[:-1]] = []
            sched[line[:-1]].append(w)
        return sched




print(doc_day())'''
class Attendee:
    def __init__(self,fname,lname,scompany,rstate,semail):
        self.f_ame = fname
        self.l_ame= lname
        self.company= scompany
        self.state = rstate
        self.email= semail
        self.attendee = []

    def getFName(self):
        return self.f_ame
    
    def getLName(self):
        return self.l_ame
    
    def getCompany(self):
        return self.company
    
    def getState(self):
        return self.state
    
    def getEmail(self):
        return self.email
    def setName(self,new_name):
        self.name= new_name
        
    def setCompany(self,new_company):
        self.company = new_company
        
    def setState(self,new_state):
        self.state= new_state
        
    def setEmail(self,new_email):
        self.email= new_email

def addAttendee():
    l = int(input("Enter what you want to do:\n"))
    f_name = (input("Name,Company,State and Email respectively:\n"))
    l_name = (input("Name,Company,State and Email respectively:\n"))
    comp =(input("Name,Company,State and Email respectively:\n"))
    tate =(input("Name,Company,State and Email respectively:\n"))
    mail = input("Name,Company,State and Email respectively:\n")
    #list =[]
    if int(l) == 1:
        '''infile = open("Homework dummy.txt","r")
        for line in infile:
            f_name,l_name,comp,tate,mail= line.split()
            mail = mail.rstrip('\n')
            f_name = Attendee(f_name,l_name,comp,tate,mail)
            
        list.append(f_name)'''
        
        new_attendee= Attendee(f_name,l_name,comp,tate,mail)
        '''list.append(new_attendee)'''
        infile = open("Homework dummy.txt","a")
        savestring= ""
        attendee = []
        attendee.append(new_attendee.getFName())
        attendee.append(new_attendee.getLName())
        attendee.append(new_attendee.getCompany())
        attendee.append(new_attendee.getState())
        attendee.append(new_attendee.getEmail())
        for word in attendee:
            savestring += word + " "
        print(savestring)
        infile.write("\n" + savestring[:-1])
        infile.close()
        print(list)
        
    

addAttendee()

'''def save_attendee():
    l = int(input("Enter what you want to do:\n"))
    f_name = input("Name,Company,State and Email respectively:\n")
    l_name = input("Name,Company,State and Email respectively:\n")
    comp =input("Name,Company,State and Email respectively:\n")
    tate =input("Name,Company,State and Email respectively:\n")
    mail = input("Name,Company,State and Email respectively:\n")
    new= Attendee(n,c,s,e)
    if int(l) == 2:
    
        infile = open("Homework dummy.txt","a")
        savestring= ""
        attendee = []
        attendee.append(new.getName())
        attendee.append(new.getCompany())
        attendee.append(new.getState())
        attendee.append(new.getEmail())
        for word in attendee:
            savestring += word + " "
            #savestring = savestring[:-1] 
        print(savestring)
        infile.write("\n" + savestring[:-1])
        infile.close()
#save_attendee()'''
        
def del_attendee():
    l = int(input("What do you want to do:\n"))
    attendee = input("Enter name of attendee:\n")
    
    if l == 3 :
        infile = open("Homework dummy.txt","r")

        for line in infile:
             f_name,l_name,comp,tate, mail= line.split()
             mail = mail.rstrip('\n')
             infile = open("Homework dummy.txt","w")
        
             if attendee != f_name:
                 infile.write(line)
            
#del_attendee()
        
        

def display_info():
    l = int(input("What do you want to do:\n"))
    if l == 6:
        attendee = input("Enter name of attendee:\n")
        infile = open("Homework dummy.txt","r")
        for person in infile:
            f_name,l_name,comp,tate, mail= person.split()
            mail = mail.rstrip('\n')
            if attendee == f_name:
                print( f_name,l_name,comp,tate, mail, end="")
                
#display_info()
            
    
def lst_attendee():
    l = int(input("What do you want to do:\n"))
    if l == 4:
        infile = open("Homework dummy.txt","r")
        for line in infile:
            f_name,l_name,comp,tate, mail= line.split()
            print(f_name + l_name)
            print(mail)
        infile.close()
        
#lst_attendee()

def lst_state():
    l = int(input("What do you want to do:\n"))
    state= input("Enter the state of the attendee:\n")
    if l == 5:
        infile = open("Homework dummy.txt","r")
        for line in infile:
            f_name,l_name,comp,tate, mail = line.split()
            if state == tate:
                print(f_name + l_name)
                print(mail)
                
#lst_state()
        
    
    
'''infile = open("Homework dummy.txt","r")
   for line in infile:
       n,c,s,e= line.split()
       e = e.rstrip('\n')
       if n == attendee:
           del(infile)
        print(list)'''      
        
        
        
        
        

    

    




    