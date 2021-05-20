#!/usr/bin/env python3
# NPR_Alarm_Clock.py
# Alarm clock that plays Morning Edition at 8:10 am every weekday
# Brendan Inglis
# May 2021

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time

# set chrome driver to open without GUI
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Using Chrome to access web without GUI
# driver = webdriver.Chrome(executable_path='./chromedriver')  # need to be on VPN???
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)  # headless (no window)

# Open the website
driver.get('https://www.npr.org/programs/morning-edition/')

# Small wait to ensure Listen Live is available
delay = 2  # seconds
#myElem = WebDriverWait(driver, delay)

try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'player-item-stream')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")  # Still works even though it is timing out

# 'Listen Live' Button
init_button = driver.find_element_by_class_name('btn-live-radio')
init_button.click()

# Insert a brief wait so the screen can expand and become findable
myElem = WebDriverWait(driver, delay)
#try:
    #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'player-item-stream')))
    #print("Page is ready!")
#except TimeoutException:
    #print("Loading took too much time!")

# Live radio play button
play_button = driver.find_element_by_class_name('player-item-stream')
play_button.click()

# Close and quit driver after 50 minutes (when morning edition is over)
time.sleep(3000)  # seconds- leave it up for 50 minutes so 3000
driver.close()
driver.quit()  # Current Issues: Only works with VPN Need to make a CRON job
