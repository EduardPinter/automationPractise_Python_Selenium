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
        self.action = ActionChains(self.driver)

    def hover_women_section(self):

        hoverElement = self.driver.find_element(*self.WOMEN_LINK)
        self.action.move_to_element(hoverElement).perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.TSHIRT_SECTION))

    def click_tshirt_section(self):

        clickElement = self.driver.find_element(*self.TSHIRT_SECTION)
        clickElement.click()


