from pages.page import BasePageStart


class LoginPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def get_page_url(self):

        return self.driver.current_url

    def get_page_title(self):

        return self.driver.title









