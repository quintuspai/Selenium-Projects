import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


email = 'Enter your Email Id here'
google_login = 'https://accounts.google.com/Login#identifier'
pasword = 'Enter your password here'
browser = None
email_list = ['recipient 1','recipient 2','recipient 3']

def gmail_login():
    global browser
    browser = webdriver.Chrome()
    browser.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
    google_login_btn = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/button[1]')))
    if google_login_btn:
        google_login_btn.click()
    else:
        print("Some issue\n")
    time.sleep(3)
    ActionChains(browser).send_keys(email).perform()
    browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
    time.sleep(4)
    ActionChains(browser).send_keys(pasword).perform()
    browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
    time.sleep(10)

def load():
    global browser, email_list
    browser.get('https://mail.google.com/mail/u/0/#inbox')
    time.sleep(7)
    ActionChains(browser).send_keys('c').perform()
    time.sleep(2)
    for mailid in email_list:
        ActionChains(browser).send_keys(mailid).perform()
        ActionChains(browser).send_keys(Keys.ENTER).perform()
        time.sleep(1)
    ActionChains(browser).send_keys(Keys.TAB).perform()
    ActionChains(browser).send_keys('Enter your subject here').perform()
    ActionChains(browser).send_keys(Keys.TAB).perform()
    ActionChains(browser).send_keys('Enter your message body here').perform()
    time.sleep(2)
    ActionChains(browser).send_keys(Keys.TAB).perform()
    ActionChains(browser).send_keys(Keys.ENTER).perform()

if __name__ == '__main__':
    browser = None
    gmail_login()
    load()
    time.sleep(4)
    browser.quit()