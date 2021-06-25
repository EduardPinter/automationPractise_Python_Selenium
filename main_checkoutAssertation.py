import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import data
from pages.mainPage import MainPage
from pages.tshirtsPage import TshirtPage
from pages.fadedTshirtPage import FadedTshirtPage


class CheckoutAssertation(unittest.TestCase):


    def setUp(self):

        self.browserName = input("Enter the browser you want to use -> ")

        if self.browserName == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif self.browserName == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            print("Browser name ==> " + self.browserName)

        self.driver.get("http://automationpractice.com/index.php")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_hover_elements(self):
        mainPage = MainPage(self.driver)
        mainPage.hover_women_section()
        mainPage.click_tshirt_section()
        tshirtPage = TshirtPage(self.driver)
        tshirtPage.click_on_faded_tshirt()
        fadedTshirtPage = FadedTshirtPage(self.driver)
        fadedTshirtPage.pick_size()
        fadedTshirtPage.pick_color()
        fadedTshirtPage.enter_quantity()
        fadedTshirtPage.add_to_cart()
        time.sleep(5)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()