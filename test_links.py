#!/usr/bin/env python
# from http://stackoverflow.com/questions/8572540/getting-all-href-from-a-code

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

ListlinkerHrefs = browser.find_elements_by_xpath("//*[@href]")

for ListlinkerHref in ListlinkerHrefs:
    print(ListlinkerHref.get_attribute('href'))
