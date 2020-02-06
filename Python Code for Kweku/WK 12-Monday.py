class AshesiStudent:
    def __init__(self):
        self.gender = ""
        self.height = ""
        self.nationality = ""
        self.first_name = ""
        self.last_name = ""
        self.dob= ""
        self.r_status = ""
        self.major = ""
        self.id = ""
        self.GPA = ""
        self.honours = 0.0
        
        
    def printc(self):
        print(self.gender)
        print(self.height)
        print(self.nationality)
        print(self.first_name)
        print(self.last_name)
        print(self.dob)
        print(self.r_status)
        print(self.major)
        print(self.id)
        
    def set_gender(self,gender_arg):
        self.gender = gender_arg
    def set_height(self,height_arg):
        self.height = height_arg
    def set_first_name(self,fname_arg):
        self.first_name= fname_arg
    def set_last_name(self,lname_arg):
        self.last_name= lname_arg
    def set_nationality(self,nationality_arg):
        self.nationality = nationality_arg
    def set_dob(self,dob_arg):
        self.dob = dob_arg
    def set_r_status(self,rstatus_arg):
        self.r_status= rstatus_arg
    def set_major(self,major_arg):
        self.major = major_arg
    def set_id(self,id_arg):
        self.id= id_arg
    def set_GPA(self,GPA_arg):
        self.GPA = GPA_arg
    def set_honours(self,honours_arg):
        self.honours= honours_arg
    
    
    def getgender(self):
        return self.gender
    
    def getheight(self):
        return self.height
    
    def getfirst_name(self):
        return self.first_name
    
    def getnationality(self):
        return self.nationality
    
    def getlast_name(self):
        return self.last_name
    
    def getdob(self):
        return self.dob
    
    def get_r_status(self):
        return self.r_status
    
    def get_major(self):
        return self.major
    
    def get_id(self):
        return self.id
    
    def get_GPA(self):
        return self.GPA
    
    def get_honours(self):
        if self.GPA >= 3.6 and self.GPA <= 3.7:
            return "Cum Laude"
        elif self.GPA >= 3.71 and self.GPA <= 3.8:
            return "Magna Cum Laude"
        elif self.GPA >= 3.81 and self.GPA <= 4.00:
            return "Summa Cum Laude"
        else:
            return "Sorry"
    

kweku= AshesiStudent()
print(kweku.gender)
kweku.gender = "male"
kweku.height = "6 ' 4"
kweku.nationality = "China"
kweku.first_name = "Kweku"
kweku.last_name = "Yamoah"
kweku.dob = "05/05/99"
kweku.r_status = "In love with Leonette"
kweku.major = "Computer Science"
kweku.id = "71712022"
kweku.GPA = 3.5
kweku.honours = "Cum Laude"

kweku.printc()