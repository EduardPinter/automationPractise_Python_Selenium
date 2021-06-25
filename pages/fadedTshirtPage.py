from pages.page import BasePageStart
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class FadedTshirtPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.SIZE = (By.ID, "group_1")
        self.COLOR = (By.NAME, "Blue")
        self.QUANTITY = (By.ID, "quantity_wanted")
        self.ADD_TO_CART = (By.XPATH, "//p[@id='add_to_cart']//span[.='Add to cart']")

    def pick_size(self):

        size = self.driver.find_element(*self.SIZE)
        sizeM = Select(size)
        sizeM.select_by_visible_text("M")

    def pick_color(self):

        color = self.driver.find_element(*self.COLOR)
        color.click()

    def enter_quantity(self):

        quantity = self.driver.find_element(*self.QUANTITY)
        quantity.clear()
        quantity.send_keys(2)

    def add_to_cart(self):

        addToCart = self.driver.find_element(*self.ADD_TO_CART)
        addToCart.click()






