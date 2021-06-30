from pages.page import BasePageStart
from selenium.webdriver.common.by import By


class CheckoutPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.DESC_COLOR_SIZE = (By.LINK_TEXT, "Color : Blue, Size : M")
        self.FADED_SHORT_SLEEVE_XPATH = (By.XPATH, '//*[@id="product_1_4_0_0"]/td[2]/p/a')
        self.TOTAL_PRICE = (By.ID, "total_product")
        self.BUTTON_PROCEED = (By.XPATH, "//div[@id='center_column']//a[@title='Proceed to checkout']/span")

    def get_text_of_element(self, element):

        return self.driver.find_element(*element).text

    def click_on_proceed(self):

        self.driver.find_element(*self.BUTTON_PROCEED).click()









