import unittest

from selenium import webdriver
from webium import BasePage

from pages.main import StartPage
from pages.subcategory import SubCategory
from pages.price import Price
from pages.sort import Sort
from pages.result import Result



def test_one111(driver_manager):
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

def test_one2222(driver_manager):
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

def test_one3333(driver_manager):
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


