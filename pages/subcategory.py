from selenium.webdriver.common.by import By
from webium import Find, BasePage


class SubCategory(BasePage):
    subcategory = Find(by=By.XPATH, value='//*[@id="content-inner-block"]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/a')

    def __init__(self):
        super(SubCategory, self).__init__(url='https://rozetka.com.ua/')