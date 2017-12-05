from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import Find, BasePage, Finds

class pricecc(WebElement):
    price = Find(by=By.CLASS_NAME, value='g-price-uah')
    #name = Find(by=By.CLASS_NAME, value='g-i-tile-i-title')
class Result(BasePage):

    price = Finds(pricecc, By.XPATH, '//*[@id="catalog_goods_block"]/div/div/div[1]')
    #price = Finds(pricecc, By.CLASS_NAME, 'g-price-uah')
    #sname = Finds(pricecc,name, By.CLASS_NAME, 'g-i-tile-i-title')


    def __init__(self):
        super().__init__(url='https://rozetka.com.ua/')

    def prices(self):
        for price in self.price:
            res = price.text.split("грн")
            print(res[0] + 'грн')
"""
'//div[@id="careers-vacancies"]/div[@data-id]'
//*[@id="jobs_list"]/div[2]/div/ul/li/ul/li[2]
//*[@id="catalog_goods_block"]/div/div[.over-wraper]/div[1]
//*[@id="catalog_goods_block"]/div/div[1-3]/div[1]
"""