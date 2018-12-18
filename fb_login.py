from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time as t
import os
from read_json import fb_email_secret, fb_password_secret

chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)
opts = ChromeOptions()
opts.binary_location = chrome_bin
driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=opts)


def login():
    driver.get('https://www.facebook.com/')
    print "Opened facebook..."
    a = driver.find_element_by_id('email')
    t.sleep(5)
    a.send_keys(fb_email_secret)
    print "Email Id entered..."
    t.sleep(5)
    b = driver.find_element_by_id('pass')
    b.send_keys(fb_password_secret)
    t.sleep(5)
    print "Password entered..."
    c = driver.find_element_by_id('loginbutton')
    c.click()
    t.sleep(5)
