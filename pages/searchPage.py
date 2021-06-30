from pages.page import BasePageStart
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.QUICK_VIEW = (By.XPATH, "//div[@id='center_column']/ul//div[@class='product-container']//div[@class='product-image-container']/a[2]/span[.='Quick view']")
        self.BLOUSE_ITEM_DESC = (By.XPATH, "//div[@id='short_description_content']/p[.='Short sleeved blouse with feminine draped sleeve detail.']")
        self.HOVER_BLOUSE_ITEM = (By.CLASS_NAME, "product_img_link")
        self.action = ActionChains(self.driver)
        self.IFRAME = (By.TAG_NAME, "iframe")

    def switch_to_iframe(self):

        iframe = self.driver.find_element(*self.IFRAME)
        self.driver.switch_to.frame(iframe)

    def hover_blouse_item(self):

        blouse_item = self.driver.find_element(*self.HOVER_BLOUSE_ITEM)
        self.action.move_to_element(blouse_item).perform()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.QUICK_VIEW))

    def quick_view_item(self):

        self.driver.find_element(*self.QUICK_VIEW).click()

    def blouse_item_desc(self):

        return self.driver.find_element(*self.BLOUSE_ITEM_DESC).text




