from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class JioWorker(object):
    """docstring for JioWorker."""
    def __init__(self):
        super(JioWorker, self).__init__()
        self._browser = None
        self.numbers = ['1234567891']  #Enter Jio numbers here /.prepaid ones
    
    def status(self):
        link = 'https://www.jio.com/selfcare/recharge/status/'
        cururl = self._browser.current_url
        assert cururl == link
    
    def arrange(self):
        self._browser = webdriver.Chrome('Path to chromedriver.exe')
        self._browser.get('https://www.jio.com/')
        
    def act(self, number):
        #print(number)
        try:
            self._browser.maximize_window()
        except:
            pass
        number_box = WebDriverWait(self._browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="last_name"]')))
        number_box.send_keys(number)
        sleep(2)
        self._browser.find_element_by_xpath('//*[@id="proceedRecharge"]').click()
        sleep(10)
        
        ##switch to 4g plans
        
        self._browser.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/button[3]').click()
        sleep(7)
        
        #click buy button for a 11 rupees plan
        
        self._browser.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/button[2]').click()
        sleep(7)
        dc = WebDriverWait(self._browser,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="DC"]')))  #Debit card option is selected
        dc.click()
        
        ##gateway reached
        cardno = WebDriverWait(self._browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="credit-card"]')))
        cardno.send_keys('Enter your Card Number')
        
        ####month
        self._browser.find_element_by_xpath('//*[@id="month_modal_wrap"]').click()
        sleep(3)
        month = self._browser.find_element_by_xpath('//*[@id="08"]/div[2]/input') # Month here used is 08
        self._browser.execute_script("arguments[0].scrollIntoView();", month)
        sleep(3)
        month.click()
        sleep(3)
        
        ####year
        self._browser.find_element_by_xpath('//*[@id="year_modal_wrap"]').click()
        sleep(3)
        year = self._browser.find_element_by_xpath('//*[@id="2022"]/div[2]/input') # Month here used is 08
        year.click()
        sleep(3)
        
        ######cvv
        cvv = self._browser.find_element_by_xpath('//*[@id="cvvNumber"]')
        cvv.send_keys('Enter CVV')
        
        #######name
        name = self._browser.find_element_by_xpath('//*[@id="cardHolderName"]')
        name.send_keys("Enter Name on card")
        
        ######
        sleep(3)
        self._browser.find_element_by_xpath('//*[@id="formsubmit"]').click()
        sleep(15)
        
        try:
            self.status()
            sleep(7)
            new_url = "https://www.jio.com/"
            self._browser.execute_script("window.open('');")
            self._browser.switch_to.window(self._browser.window_handles[1])
            self._browser.get(new_url)
            self._browser.switch_to.window(self._browser.window_handles[0])
            self._browser.close()
            self._browser.switch_to.window(self._browser.window_handles[0])
            sleep(7)
        except:
            print("Some Error occured")
            sleep(7)
            new_url = "https://www.jio.com/"
            self._browser.execute_script("window.open('');")
            self._browser.switch_to.window(self._browser.window_handles[1])
            self._browser.get(new_url)
            self._browser.switch_to.window(self._browser.window_handles[0])
            self._browser.close()
            self._browser.switch_to.window(self._browser.window_handles[0])
            sleep(7)
        
    def perform_recharges(self):
        for _,val in enumerate(self.numbers):
            self.act(val)
            sleep(7)  
        
    def close(self):
        self._browser.close()
        
        
        
if __name__ == "__main__":
    worker = JioWorker()
    worker.arrange()
    worker.perform_recharges()
    worker.close()
