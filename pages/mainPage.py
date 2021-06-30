import time
from pages.page import BasePageStart
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.WOMEN_LINK = (By.XPATH, "//div[@id='block_top_menu']/ul//a[@title='Women']")
        self.TSHIRT_SECTION = (By.XPATH, "//div[@id='block_top_menu']/ul/li[1]/ul/li[1]/ul//a[@title='T-shirts']")
        self.SEARCH_INPUT_FIELD = (By.ID, "search_query_top")
        self.SEARCH_BUTTON = (By.NAME, "submit_search")
        self.NEXT_BUTTON = (By.CLASS_NAME, "bx-next")
        self.SLIDER_SELECTOR = (By.CSS_SELECTOR, "#homeslider")
        self.SLIDER_SCREENSHOT = (By.CSS_SELECTOR, "#homepage-slider")
        self.SRC_RED_DRESS = (By.CSS_SELECTOR, "#homeslider > li:nth-child(4) > a > img")
        self.action = ActionChains(self.driver)

    def hover_women_section(self):

        hoverElement = self.driver.find_element(*self.WOMEN_LINK)
        self.action.move_to_element(hoverElement).perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.TSHIRT_SECTION))

    def click_tshirt_section(self):

        clickElement = self.driver.find_element(*self.TSHIRT_SECTION)
        clickElement.click()

    def search_bar(self, word):

        self.driver.find_element(*self.SEARCH_INPUT_FIELD).send_keys(word)

    def click_search_button(self):

        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def click_next_button_slider(self):

        self.driver.find_element(*self.NEXT_BUTTON).click()
        time.sleep(1)

    def slider_css_property(self):

        return self.driver.find_element(*self.SLIDER_SELECTOR).value_of_css_property("left")

    def src_property(self):

        return self.driver.find_element(*self.SRC_RED_DRESS).get_attribute("src")

    def screenshot_element(self):

        screenshotElement = self.driver.find_element(*self.SLIDER_SCREENSHOT)
        screenshotElement.screenshot("1.png")

