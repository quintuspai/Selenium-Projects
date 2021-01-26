from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class WhatsAppSender(object):
    """docstring for WhatsAppSender."""
    def __init__(self):
        super(WhatsAppSender, self).__init__()
        self.browser = None
    
    def whats_app_login(self):
        try:
            self.browser = webdriver.Chrome("c:\\webdrivers\\chromedriver.exe")
            browser.get("https://web.whatsapp.com/")
            time.sleep(6)
        except:
            pass
    
    def send_message(self, message):
        try:
            time.sleep(3)
            input_box = self.browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(message + Keys.ENTER)
            time.sleep(2)
        except:
            pass
    
    def send_image(self, caption):
        full_path = 'Path to image' #example c:\\pqr\\image.png
        try:
            self.browser.find_element_by_xpath('//div[@title = "Attach"]').click()
            time.sleep(1)
            self.browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(full_path)
            time.sleep(3)
            add_caption = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div/div[2]/div/div[3]/div[1]')
            add_caption.send_keys(caption)
            time.sleep(1)
            self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click()
            time.sleep(3)
        except:
            pass
        
    def send_file(self):
        full_path = "Path to the file" #example c:\\abc\\1.txt
        try:
            time.sleep(3)
            self.browser.find_element_by_xpath('//div[@title = "Attach"]').click()
            file_box = self.browser.find_element_by_xpath('//input[@accept="*"]')
            file_box.send_keys(full_path)
            time.sleep(3)
            self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click()
            time.sleep(2)
        except:
            pass
    
    def sender(self,contacts, message, image_caption):
        for i in contacts:
            link = "https://wa.me/"+i
            self.browser.get(link)
            time.sleep(4)
            try:
                self.browser.find_element_by_xpath('//*[@id="action-button"]').click()
                time.sleep(1)
                self.browser.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
                time.sleep(3)
            except:
                pass
            time.sleep(2)
            try:
                self.send_message(message)
                time.sleep(2)
                self.send_image(image_caption)
                time.sleep(2)
                self.send_file()
                time.sleep(2)
            except:
                pass
        self.browser.quit()

if __name__ == '__main__':
    message = 'Greetings. Message sent through python. :)'  #Add your message here
    image_caption = 'This is a caption'  #Add a caption here
    contacts = ['911234567890','910987654321'] #Add the mobile numbers to the list prefixed with 91   .The ones added in the list are dummy numbers. 
    WaHelper = WhatsAppSender()
    WaHelper.whats_app_login()
    WaHelper.sender(contacts, message, image_caption)