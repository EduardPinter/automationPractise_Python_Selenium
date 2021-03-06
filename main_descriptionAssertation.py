import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import data
from pages.mainPage import MainPage
from pages.searchPage import SearchPage



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

    def test_description_assertation(self):
        mainPage = MainPage(self.driver)
        mainPage.search_bar(data.DescriptionAssert.search_item)
        mainPage.click_search_button()
        searchPage = SearchPage(self.driver)
        searchPage.hover_blouse_item()
        searchPage.quick_view_item()
        searchPage.switch_to_iframe()
        self.assertEqual(searchPage.blouse_item_desc(), data.DescriptionAssert.blouse_item_desc)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()