import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import data
from pages.mainPage import MainPage


class ScreenshotElement(unittest.TestCase):

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

    def test_screenshot_red_dress(self):
        mainPage = MainPage(self.driver)
        mainPage.click_next_button_slider()
        mainPage.click_next_button_slider()
        self.assertEqual(mainPage.slider_css_property(), data.ScreenshotAssert.pixelsRedDress)
        self.assertEqual(mainPage.src_property(), data.ScreenshotAssert.srcOfPicture)
        mainPage.screenshot_element()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()