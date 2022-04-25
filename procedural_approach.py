#%% Importing necessary modules
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains

#%% Instantiating webdriver class
# executable_path should be of form '/Users/tinder-selenium/chromedriver'
# Chromedriver file does not have any extension
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Getting to desired page
driver.get('https://tinder.com/')

# Try to press right arrow once
driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)

# Putting right arrow click into loop
for i in range(100):
    driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
    sleep(0.5)
