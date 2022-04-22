#%% Importing necessary modules
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains

#%% Instantiating webdriver class
driver = webdriver.Chrome(executable_path='/Users/milanmitrovic/PycharmProjects/tinder-selenium/chromedriver')

# Getting to desired page
driver.get('https://tinder.com/')

# Try to press right arrow once
driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)

# Putting right arrow click into loop
for i in range(100):
    driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
    sleep(0.5)
