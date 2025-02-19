import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def startBot(username, password, url):
    path = path = os.path.join(os.getcwd(), "chromedriver-win64", "chromedriver.exe")
    service = Service(path)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get(url)
    time.sleep(7)
    driver.find_element(By.ID, "login_field").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "commit").click()
    
    time.sleep(5)
    
    quit()
    
#Enter your login credentials
username = "nicolasgabrielmartins"
password = "password"

url = "https://github.com/login"
    
startBot(username, password, url)