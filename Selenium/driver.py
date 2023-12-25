import os
import sys

from dotenv import find_dotenv, load_dotenv
from selenium import webdriver


load_dotenv(find_dotenv())

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def get_driver(self):
        return self.driver
    
    def quit_driver(self):
        return self.driver.quit()