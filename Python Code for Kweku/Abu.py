# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:02:27 2019

@author: User
"""

print("Welcome to La cave Housing an Properties\n")
print("What is your name\n")
cus_name = input("Name of Cutsomer:")
print("hello" + cus_name + "Would you like to make a purchase?")
pur_response =input("Response:")
if pur_response == "Yes":
    cash_hand = eval(input("Enter amount:\n"))
    good_credit = cash_hand >= 500000
    bad_credit = cash_hand < 500000
    print(type(good_credit))
    if cash_hand == good_credit:
        print("Eligible for discount of 10%")
        float(good_credit)
    else:
        print("you are eligible for a 30% dicount")
        float(bad_credit)
else:
    print("Do come again next time")