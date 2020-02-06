# This program generates an e-mail for Ashesi students and faculty
print("Hello, wlecome to the e-mail generator")
ashesi_community = input("Please enter 's' if you are a student or 'l' if you are a faculty member: ")
print()

f_name = input("Enter your first name:\n")
print()
l_name = input("Enter your last name:\n")

if ashesi_community == "s":
    print (f_name.lower() + "." + l_name.lower() + "@ashesi.edu.gh")
    
elif ashesi_community == "l":
    print (f_name[0].lower() + l_name.lower() + "@ashesi.edu.gh")
    
else:
    print("You are not a part of our community. Go on with the demonstration in KNUST")