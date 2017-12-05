from selenium.webdriver.common.by import By
from webium import Find, BasePage


class StartPage(BasePage):

    category = Find(by=By.XPATH, value='//*[@id="2416"]/a')
    def __init__(self):
        super().__init__(url='https://rozetka.com.ua/')


