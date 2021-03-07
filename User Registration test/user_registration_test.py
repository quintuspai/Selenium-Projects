import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = None

def arrange():
    '''
     starts webbrowser and navigates to the site
    '''
    global browser
    browser = webdriver.Chrome('D:\\webdrivers2\\chromedriver.exe')
    browser.get('https://docket-test.herokuapp.com/register')

def act():
    '''
    Completes the registration process and clicks the register button
    '''
    global browser
    uname = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
    uname.send_keys("user1")
    browser.find_element_by_xpath('//*[@id="email"]').send_keys("12@gmail.com")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys("1234")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="password2"]').send_keys('1234')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(3)

def registered():
    '''
    Asserts if registration was successful and user was directed to login page
    '''
    global browser
    message = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[1]').text
    
    assert message == "Congratulations, you are now registered"
    
    cururl = browser.current_url
    assert cururl == "https://docket-test.herokuapp.com/login"
    
    browser.quit()
    
    

if __name__ =="__main__":
    arrange()
    act()
    registered()