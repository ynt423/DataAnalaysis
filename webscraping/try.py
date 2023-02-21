from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:/Users/Oscar Yu/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
""" driver.get("http://www.google.com") """

driver.get("http://www.dcard.tw/f")
time.sleep(5)
""" search = driver.find_element("name", "query")
search.send_keys("比特幣")
search.send_keys(Keys.RETURN) """

titles = driver.find_elements("class_name", "atm_cs_1urozh")
for title in titles:
    print(title.text)

time.sleep(10)

input()
