
#%% Importing necessary modules
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains


#%% Creating class structure that will contain functions and 
# store data regarding browser instance 
class DriverClass:
    def __init__(self, driver_path='/Users/milanmitrovic/PycharmProjects/tinder-selenium/chromedriver'):
        self.drive_path = driver_path
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def get_to_tinder(self):
        self.driver.get('https://tinder.com/')

    def click_righ_arrow(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)

    def loop_right_arrow(self, number_of_times):
        for i in range(number_of_times):
            self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            sleep(0.5)


#%% Instantiating class i.e. opening browser
d1 = DriverClass()


#%% Going to desired page
d1.get_to_tinder()

#%% Performing loop
# Right clicking desired number of times
d1.loop_right_arrow(1000)

