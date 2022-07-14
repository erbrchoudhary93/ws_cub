from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try :
            if partest[i] !=  usertest[i]:
                error = error + 1
        except:
            error = error+1
            
    return error
    
    
def speed_time(time_start,time_end,user_input):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay,2)
    speed = len(user_input)/time_roundoff
    return round(speed)

if __name__ =='__main__':    
    while True:
        ck = input("Ready to test  : yes/no   :  ")

        if ck== "yes":

            test = ["He is nice guy . he is good in python programming . He is also good in django","I am good in c and c++ also"]

            test1 = r.choice(test)
            print("*******************************Typing speed calculator*************************************")
            print(test1)
            print()
            print()

            time_1 = time()

            test_input = input("Enter : ")

            time_2 = time()

            print("Speed : " , speed_time(time_1,time_2,test_input) , "Word per second")
            print("Error :  ", mistake(test1,test_input))
            
        elif ck == "no":
            print("Thank You ")
            break
        else: 
            print("Wrong input ")