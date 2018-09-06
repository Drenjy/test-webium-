import unittest

from selenium import webdriver
from webium import BasePage

from pages.main import StartPage
from pages.subcategory import SubCategory
from pages.price import Price
from pages.sort import Sort
from pages.result import Result

class Test(unittest.TestCase):

    def setUp(self):
        BasePage._driver = webdriver.Remote(command_executor='http://192.168.56.1:4444/wd/hub',desired_capabilities={'browserName':'chrome'})
        BasePage._driver.implicitly_wait(10)

    def test_one366544(self):
        page = StartPage()
        page.open()
        page.category.click()
        subcategory = SubCategory()
        subcategory.subcategory.click()
        price = Price()
        #price.price(400, 500)
        _sort = Sort()
        _sort.sort1()
        #_sort.sort.click()
        #_sort.subsort.click()
        _result = Result()
        _result.prices()

    def test_one245443(self):
        page = StartPage()
        page.open()
        page.category.click()
        subcategory = SubCategory()
        subcategory.subcategory.click()
        price = Price()
        #price.price(400, 500)
        _sort = Sort()
        _sort.sort1()
        #_sort.sort.click()
        #_sort.subsort.click()
        _result = Result()
        _result.prices()

    def test_one34443(self):
        page = StartPage()
        page.open()
        page.category.click()
        subcategory = SubCategory()
        subcategory.subcategory.click()
        price = Price()
        # price.price(400, 500)
        _sort = Sort()
        _sort.sort1()
        # _sort.sort.click()
        # _sort.subsort.click()
        _result = Result()
        _result.prices()




    def tearDown(self):
        BasePage._driver.close()

java -Dwebdriver.chrome.driver=D:\rozetka.pytest\resources\chromedriver.exe -Dwebdriver.gecko.driver=D:\geckodriver.exe -jar selenium-server-standalone-3.8.1.jar -role node -hub http://192.168.56.1:4444/grid/register/
java -Dwebdriver.chrome.driver=D:\rozetka.pytest\resources\chromedriver.exe -Dwebdriver.gecko.driver=D:\geckodriver.exe -jar selenium-server-standalone-3.8.1.jar -role node -nodeConfig nodeconfig.json
## "java -jar selenium-server-standalone-3.8.1.jar -role hub -cleanUpCycle 5000 -timeout 2"
java -jar selenium-server-standalone-3.8.1.jar -role hub -hubConfig hubconfig.json -debug