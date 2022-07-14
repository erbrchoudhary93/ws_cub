# this program cheak all condition of email pattrn
# a-z small case
#0-9 
#. _ Time 1
# @ time 1 
# . 2nd or third position
k=0
j=0
d=0
email = input("Enter your Email :  ")
if len(email)>=6: # first condition 
    
    if email[0].isalpha(): # 2nd cndition
        
        if ("@" in email) and (email.count("@")==1): #3rd condition
            
            if (email[-4]==".") ^ (email[-3]=="."):  # EXor operator
                for i in email:
                    if i==i.isspace():
                        k=1
                        
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                            
                    elif i.isdigit():
                        continue
                    
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                        
                if k==1 or j==1 or d==1:
                    print("Wrong Input 'Upper case or space present or speciaal charactor present'")
                else:
                    print("Right email")
                    
            else:
                print("Wrong Email  - 'Dot is not present at the ending of email'")
        else:
            print("Wrong Email - '@ not persen or present more then one time'")
    else:
        print("Wrong Email 'First characer is not alphabet' ")
else:
    print("Wrong Email 'Email size less then 6 character' ")
