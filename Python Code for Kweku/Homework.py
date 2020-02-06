# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:24:18 2019

@author: Kweku Andoh Yamoah(71712022)
"""

class Attendee:
    def __init__(self,fname,lname,scompany,rstate,semail):
        self.f_ame = fname
        self.l_ame= lname
        self.company= scompany
        self.state = rstate
        self.email= semail
        

    
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
        
class User:
    def __init__(self, filename):
        self.infile_name = filename
        
    def addAttendee(self):
        f_name = (input("First Name:\n"))
        l_name = (input("Last Name:\n"))
        comp =(input("Company:\n"))
        tate =(input("State:\n"))
        mail = input("Email address:\n")
        
        new_attendee= Attendee(f_name,l_name,comp,tate,mail)
        
        infile = open(self.infile_name,"a")
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
        print("You have added" +" "+ f_name + " "+ l_name + " successfully")
             
    def del_attendee(self):
        attendee = input("Enter name of attendee:\n")
        infile = open(self.infile_name,"r")
        lines = infile.readlines()
        infile = open(self.infile_name,"w")
        for line in lines:
            f_name,l_name,comp,tate, mail= line.split()
            mail = mail.rstrip('\n')
            
        
            if attendee != f_name:
                infile.write(line)
                return (f_name + " " + l_name + " " + "deleted succesfully")
      
        return ("Attendee not found")
                    
    def display_info(self):
            attendee = input("Enter name of attendee:\n")
            infile = open(self.infile_name,"r")
            for person in infile:
                f_name,l_name,comp,tate, mail= person.split()
                mail = mail.rstrip('\n')
                if attendee == f_name:
                    print("Name:",f_name + " "+ l_name)
                    print("Company of", attendee, "is " + comp)
                    print("State of", attendee, "is " + tate)
                    print("Email of", attendee, "is " + mail)
                else:
                    print("\n Attendee not found")
                    
    def lst_attendee(self):
            infile = open(self.infile_name,"r")
            for line in infile:
                f_name,l_name,comp,tate, mail= line.split()
                print("Attendee name:" +f_name + " " + l_name, 
                      ",Email is:" + mail)
            infile.close()
                
    def lst_state(self):
        state= input("Enter the state of the attendee:\n")
        infile = open(self.infile_name,"r")
        for line in infile:
            f_name,l_name,comp,tate, mail = line.split()
            if state == tate:
                print("Attendee from" + " " + state + " " + "is \n")
                print(f_name + " " + l_name)
                print("You can mail the person using the following address,"
                      + " " + mail)
            
            return "Attendee not found"
            
                
                
                
                
def printIntro():
    print("Welcome to the attendee program")
    print("Hit (1) to add an attendee:\n")
    print("Hit (2) to delete an attendee:\n")
    print("Hit (3) to display info of an attendee:\n")
    print("Hit (4) to list an attendee and email:\n")
    print("Hit (5) to list an attendee from a given state with mail:\n")
                  
def main():
    printIntro()
    option = int(input("Enter what you want to do:\n"))
    file_use = "Homework dummy.txt"
    use = User(file_use)
    if option == 1:
        print("You are adding an Attendee")
        use.addAttendee()
    elif option == 2:
        print("You are deleting an attendee")
        use.del_attendee()
    elif option == 3:
        print("You are display all information on a specific attendee")
        use.display_info()
    elif option == 4:
        print("You are displaying the names and email of all attendees")
        use.lst_attendee()
    elif option == 5:
        print("You are getting name and mail of an"
              " attendee from a given state")
        use.lst_state()
    else:
        print("Enter a valid integer\n")
        print("Trying again...\n")
        main()
    
main()
    
        
    
        
        