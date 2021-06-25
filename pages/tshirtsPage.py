from pages.page import BasePageStart
from selenium.webdriver.common.by import By


class TshirtPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.TSHIRT = (By.XPATH, "//div[@id='center_column']/ul//div[@class='product-container']//h5/a[@title='Faded Short Sleeve T-shirts']")

    def click_on_faded_tshirt(self):

        self.driver.find_element(*self.TSHIRT).click()





