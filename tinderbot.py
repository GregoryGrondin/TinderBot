from selenium import webdriver
from time import sleep
import random
from secrets import usr, pwd

class TinderBot():
    def __init__(self):
        fp = webdriver.FirefoxProfile()
        fp.set_preference('permissions.default.desktop-notification', 1)
        fp.set_preference('permissions.default.geo', 1)
        fp.set_preference('geo.wifi.uri', 'https://location.services.mozilla.com/v1/geolocate?key=%MOZILLA_API_KEY%')
        self.driver = webdriver.Firefox(fp)

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(7)
        print("Actions in page 1...")
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()
        
        base_window = self.driver.window_handles[0]
        log_window = self.driver.window_handles[1]
        self.driver.switch_to.window(log_window)
        
        sleep(3)
        print("Actions in page 2...")
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        
        email_in.send_keys(usr)
        password_in.send_keys(pwd)
        login_btn.click()

        self.driver.switch_to.window(base_window)
        sleep(5)
        print("Actions in page 1...")
        location = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        location.click()
        sleep(2)
        notification = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
        notification.click()
        print("Wait now...")
        sleep(10)
    
    def like(self):
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def unlike(self):
        unlike_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        unlike_btn.click()

    def chose(self):
        r = random.randint(0, 10)
        if (r <= 8):
            self.like()
        else:
            self.unlike()
        

    def automate(self):
        while (1):
            r = random.randint(1, 3)
            sleep(r)
            try:
                self.chose()
            except Exception:
                print("Sounds like you're out of like bro, bye !")
                exit(0)
        

        
bot = TinderBot()
bot.login()
bot.automate()