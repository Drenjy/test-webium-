from selenium.webdriver.common.by import By
from webium import Find, BasePage
import time


class Sort(BasePage):

    #sort = Find(by=By.LINK_TEXT, value='по рейтингу')
    #subsort = Find(by=By.LINK_TEXT, value='от дешевых к дорогим')
    sort = Find(by=By.XPATH, value='//*[@id="sort_view"]/a')
    subsort = Find(by=By.XPATH, value='//*[@id="filter_sortcheap"]/a')
    memory = Find(by=By.XPATH, value='//*[@id="filter_20863_755001"]/label/a')

    def __init__(self):
        super().__init__(url='https://rozetka.com.ua/')
    def sort1(self):
        self.memory.click()
        time.sleep(1)
        self.sort.click()
        self.subsort.click()
        time.sleep(1)
