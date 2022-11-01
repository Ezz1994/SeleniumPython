import time

from selenium import webdriver
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Test.POMdemo.Pages.LoginPage import LoginPage
from Test.POMdemo.Pages.HomePage import HomePage
import unittest
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/user/PycharmProjects/pythonProject/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

# driver = webdriver.Chrome("../drivers/chromedriver.exe")

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.login()

        homepage = HomePage(driver)
        homepage.click_welcome_link()
        homepage.click_logout()
        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # self.driver.find_element(By.XPATH,
        #                     "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//p[contains(text(),'Paul Collings')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Completed!")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/user/PycharmProjects/pythonProject/reports"))

