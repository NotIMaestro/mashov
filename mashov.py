from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

#opens the browser & website
browser = webdriver.Firefox(executable_path = "/app/vendor/geckodriver/geckodriver.exe")
browser.maximize_window()
browser.get("https://web.mashov.info/students/login")
time.sleep(2)

#types the school name
school = browser.find_element_by_xpath("//input[@id='mat-input-3']")
school.send_keys("זיו אור נתניה")
school.send_keys(Keys.ENTER)
time.sleep(2)



#types username
username = browser.find_element_by_xpath("//*[@id='mat-input-0']")
username.send_keys('USERNAME HERE')
username.send_keys(Keys.ENTER)
time.sleep(2)



#types password
password = browser.find_element_by_xpath('//*[@id="mat-input-4"]')
password.send_keys('PASSWORD HERE')
password.send_keys(Keys.ENTER)
time.sleep(2)



#clicks submit/continue button
submit = browser.find_element_by_xpath('//*[@id="mainMenu"]/ul/li[2]/button/span/div')
submit.click()
time.sleep(2)

#clicks corona button
corona = browser.find_element_by_xpath('//*[@id="mainMenu"]/ul/li[2]/button/span/div/span/span')
corona.click()
time.sleep(2)



#click both corona side buttons
time.sleep(2)
button1 = browser.find_elements_by_class_name('mat-checkbox-label')
for x in range(0,len(button1)):
    if button1[x].is_displayed():
       button1[x].click()
        
    
#submit the corona application
    time.sleep(2)
submit2 = browser.find_element_by_xpath('//*[@id="mainView"]/mat-sidenav-content/mshv-students-covid-clearance/mat-card/mat-card-actions/button')
submit2.click()

time.sleep(5)


#closes the browser
browser.close()




            

        
