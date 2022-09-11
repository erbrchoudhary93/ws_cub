import undetected_chromedriver as uc
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.support.ui import WebDriverWait
from csv import reader
from selenium.common.exceptions import NoSuchElementException

def find_to_click_recovery_email(browser,b):
    try:
        return browser.find_element(By,CSS_SELECTOR,b)
    except NoSuchElementException:
        return None

def connecting_to_brouser(email_id,email_pass):
    if email_id != " " and email_pass != " ":
        # browser = webdriver.Chrome("chromedriver.exe")
       
        browser = uc.Chrome(use_subprocess=True)
        
        wait = WebDriverWait(browser,20)
        # browser = webdriver.Firefox()
        try:
            browser.get('https://accounts.google.com/v3/signin/identifier?dsh=S-1962633519%3A1661339028881682&continue=https%3A%2F%2Fmail.google.com&ec=GAlAFw&hl=en-GB&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession')
            # email_field = browser.find_element_by_id('identifierId')
            
            
            # wait.until(ec.invisibility_of_element_located((By.NAME,'identifier'))).send_keys(email_id)
            # wait.until(ec.invisibility_of_element_located((By.NAME,'password'))).send_keys(email_pass)
            
            email_field = browser.find_element(By.ID, "identifierId")
            
            
            
            
            email_field.clear()
            
            email_field.send_keys(email_id)
            
            email_next_button = browser.find_element(By.ID, "identifierNext")
            # fruits = driver.find_element(By.ID, "identifierNext")

            email_next_button.click()
            
            time.sleep(10)
            # input()
            
            # password_field =browser.find_element(By.ID, "password")
            try:
                password_field =browser.find_element(By.NAME, "Passwd")
            except Exception as e:
                print(e)
            try:
                password_field1 =browser.find_element(By.NAME, "password")
            except Exception as e:
                print(e)
            if password_field:
                password_field.send_keys(email_pass)
                
            else:
                password_field1.send_keys(email_pass)
                
                
            password_field.clear()
            print("password  : ",email_pass)
            
            password_field.send_keys(email_pass)
            
            # input()
            
            
            password_next_button = browser.find_element(By.ID, "passwordNext")
            password_next_button.click()
            
            time.sleep(3)
            # input()
            
            
            browser.get("https://www.youtube.com/channel/UCdnv3Qbzg8Tu4NWfMA2rNYg")
            
            
            
            
            # subcribe_next_button = browser.find_element_by_class_name("style-scope ytd-subscribe-button-renderer")
            subcribe_next_button = browser.find_element(By.CLASS_NAME, "style-scope ytd-subscribe-button-renderer")
            
            subcribe_next_button.click()
            
            time.sleep(10)
            browser.quit()
        except Exception as e:
            print(e)
            browser.quit()
            
    

with open ('email_pass1.csv') as read_obj:
    csv_reader =reader(read_obj)
    list_of_rows =list(csv_reader)
    
    

list_len = len(list_of_rows)
ids_pass_list = list_of_rows

for i in range(len(ids_pass_list)):
    id_str = ids_pass_list[i][0]
    id_pass = ids_pass_list[i][1]
    print(i)
    print("Login Id : ",id_str)  
    print("Login Password : ",id_pass)  
    
    connecting_to_brouser(id_str,id_pass)  
    
    
    
    