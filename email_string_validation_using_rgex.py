# a-z small case
#0-9 
#. _ Time 1
# @ time 1 
# . 2nd or third position
# 1st alphabet

import re # import regex module
email_Condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter Your Email :  ")

if re.search(email_Condition,user_email):
    print("Right Email")
    
else:
    print("Wrong Email ")