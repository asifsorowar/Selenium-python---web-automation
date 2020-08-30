# automation with selenium.
# asifsorowar
# code - 1
# basic selenium initialization


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.youtube.com')

searchBox = driver.find_element_by_xpath('//input[@id="search"]')
searchBox.clear()
searchBox.send_keys('i love bangladesh')
searchBox.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
