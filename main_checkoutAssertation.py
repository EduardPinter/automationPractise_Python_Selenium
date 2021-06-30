import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import data
from pages.mainPage import MainPage
from pages.tshirtsPage import TshirtPage
from pages.fadedTshirtPage import FadedTshirtPage
from pages.checkoutPaymentPage import CheckoutPage
from pages.proceedCheckout import LoginPage


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

    def test_checkout_assertation(self):
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
        self.assertEqual(fadedTshirtPage.get_text_of_element(fadedTshirtPage.SHOPPING_CART_TITLE), data.CheckoutAssert.shoppingCartTitle)
        self.assertEqual(fadedTshirtPage.get_text_of_element(fadedTshirtPage.SHOPPING_CART_ATTR), data.CheckoutAssert.shoppingCartAttr)
        self.assertEqual(fadedTshirtPage.get_text_of_element(fadedTshirtPage.SHOPPING_CART_QUANTITY), data.CheckoutAssert.shoppingCartQuantity)
        self.assertEqual(fadedTshirtPage.get_text_of_element(fadedTshirtPage.SHOPPING_CART_PRICE), data.CheckoutAssert.shoppingCartCost)
        fadedTshirtPage.proceed_to_checkout()
        checkoutPage = CheckoutPage(self.driver)
        self.assertEqual(checkoutPage.get_text_of_element(checkoutPage.FADED_SHORT_SLEEVE_XPATH), data.CheckoutAssert.shoppingCartTitle)
        self.assertEqual(checkoutPage.get_text_of_element(checkoutPage.DESC_COLOR_SIZE), data.CheckoutAssert.descColorSize)
        self.assertEqual(checkoutPage.get_text_of_element(checkoutPage.TOTAL_PRICE), data.CheckoutAssert.shoppingCartCost)
        checkoutPage.click_on_proceed()
        loginPage = LoginPage(self.driver)
        self.assertEqual(loginPage.get_page_title(), data.CheckoutAssert.loginTitle)
        self.assertEqual(loginPage.get_page_url(), data.CheckoutAssert.loginPageUrl)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()