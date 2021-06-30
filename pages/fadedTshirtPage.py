from pages.page import BasePageStart
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FadedTshirtPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.SIZE = (By.ID, "group_1")
        self.COLOR = (By.NAME, "Blue")
        self.QUANTITY = (By.ID, "quantity_wanted")
        self.ADD_TO_CART = (By.XPATH, "//p[@id='add_to_cart']//span[.='Add to cart']")
        self.SHOPPING_CART_TITLE = (By.ID, "layer_cart_product_title")
        self.SHOPPING_CART_ATTR = (By.ID, "layer_cart_product_attributes")
        self.SHOPPING_CART_QUANTITY = (By.ID, "layer_cart_product_quantity")
        self.SHOPPING_CART_PRICE = (By.ID, "layer_cart_product_price")
        self.PROCEED_TO_CHECKOUT = (By.XPATH, "/html//div[@id='layer_cart']//a[@title='Proceed to checkout']/span")
        self.FADED_SHORT_SLEEVE_LINK_TEXT = (By.LINK_TEXT, "Faded Short Sleeve T-shirts")

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
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SHOPPING_CART_TITLE))

    def get_text_of_element(self, element):

        return self.driver.find_element(*element).text

    def proceed_to_checkout(self):

        self.driver.find_element(*self.PROCEED_TO_CHECKOUT).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FADED_SHORT_SLEEVE_LINK_TEXT))

    def click_on_proceed(self):

        self.driver.find_element(*self.BUTTON_PROCEED).click()








