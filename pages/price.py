from selenium.webdriver.common.by import By
from webium import Find, BasePage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

class Textfield(WebElement):
    def __init__(self):
        super().__init__(url='https://rozetka.com.ua/')
    def text(self):
        return self.get_attribute('value')

class Price(BasePage):
    min = Find(Textfield, By.XPATH, value='//*[@id="price[min]"]')
    max = Find(Textfield, By.XPATH, value='//*[@id="price[max]"]')
    ok = Find(by=By.ID, value='submitprice')

    def price(self,min,max):
        self.min.send_keys(min)
        self.min.send_keys(Keys.TAB)
        self.max.send_keys(max)
        self.ok.click()

