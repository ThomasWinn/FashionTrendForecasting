import csv
import os
import random
import sys
import time

from dotenv import find_dotenv, load_dotenv

from driver import Driver


load_dotenv(find_dotenv())

class Instagram_Bot:
    def __init__(self, ig_account_path):
        self.driver = Driver.get_driver()
        
        self.instagram_url = 'https://instagram.com'
        
        self.username = os.environ.get('INSTAGRAM_USERNAME')
        self.password = os.environ.get('INSTAGRAM_PASSWORD')
        
        self.account_path = ig_account_path
        
    def get_account_list(self):
        lst = []
        with open(self.account_path, newline='') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                lst.append(row['Account'])
        
        return lst
    
    def login(self):
        self.driver.get(self.instagram_url)
        time.sleep(get_random_time())
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(self.password)
        time.sleep(get_random_time())      
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        
        
def get_random_time():
    return random.randint(3, 5)
    
if __name__ == "__main__":
    x = Instagram_Bot('../Accounts/instagram_accounts.csv')
    accounts = x.get_account_list()
    print(accounts)