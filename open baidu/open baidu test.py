#test open baidu link
import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://start.firefoxchina.cn/")
driver.find_element_by_id("search-key").send_keys("中国")
driver.find_element_by_id("search-submit") .click()
time.sleep(10)
driver.close()

