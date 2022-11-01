from selenium.webdriver.common.by import By
from Test.POMdemo.Locators.locators import Locators


class HomePage():

    def __init__(self,driver):
        self.driver=driver

        self.welcome_link_xpath = Locators.welcome_link_xpath
        self.logout_linkbutton_xptah = Locators.logout_linkbutton_xptah

    def click_welcome_link(self):
        self.driver.find_element(By.XPATH,self.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_linkbutton_xptah).click()
