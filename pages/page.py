from pages.element import BasePageElement


class BasePageStart(BasePageElement):
    class BasePage(object):

        def __init__(self, driver):
            self.driver = driver
