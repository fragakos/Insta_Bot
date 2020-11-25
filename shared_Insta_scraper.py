from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import sub
from decimal import Decimal
import random

comment_list = []
comment_list.append("Tags here")
comment_list.append("Different tags here")
comment_list.append("Different tags here")
#   .
#   .
#   .
#   .
class Instabot:
    def __init__(self,username,password):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath("//button[text()='Accept']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username) #Login info
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password) #Login info
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(5)
        
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(5)
        self.driver.get("https://www.instagram.com/p/CH-MgQOn-7E/")
        sleep(2)
        count = 0
        while(1):
            comment = random.choice(comment_list)
            cmt = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button")
            cmt.click()
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(comment)
            sleep(2)
            post = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button")
            post.click()
            count = count + 1
            print("success" ,count, "comments")
            temp = random.randint(1,10)
            if temp % 2 == 0:
                sleep_time = 50 - (random.randint(1,2)*temp)
                print("Wait " ,sleep_time, "seconds")
                sleep(sleep_time)
                
            else:
                sleep_time = 70 - (2*temp + random.randint(1,30))
                print("Wait " ,sleep_time, "seconds")
                sleep(sleep_time)


Instabot('instagram_mail','instagram_password')
      