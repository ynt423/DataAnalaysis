
# 爬取ig關鍵字圖片
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget


PATH = "C:/Users/Oscar Yu/Desktop/chromedriver_win32/chromedriver.exe"
""" PATH = "C:/Users/hibyby/Desktop/chromedriver_win32/chromedriver.exe" """
""" driver = webdriver.Chrome(PATH) """


def main():
    option = webdriver.ChromeOptions()
    """ option.add_argument("--kiosk") """
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument('log-level=3')
    driver = webdriver.Chrome(options=option)
    driver.get("https://www40.polyu.edu.hk/poss/secure/login/loginhome.do")
    """ //*[@id="loginform"]/div[2]/table/tbody/tr/td[1]/input[2] """
    username = driver.find_element(
        "xpath", '//*[@id="loginform"]/div[2]/table/tbody/tr/td[1]/input[2]')
    password = driver.find_element(
        "xpath", '//*[@id="loginform"]/div[2]/table/tbody/tr/td[1]/input[3]')
    #login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    login = driver.find_element(
        "xpath", '//*[@id="loginform"]/div[2]/table/tbody/tr/td[2]/button')

    username.clear()
    password.clear()
    username.send_keys('20048665D')
    password.send_keys('Xsw21qaz')
    login.click()
    time.sleep(5)
    """ /html/body/header/div/nav/ul/li[7]/a/span """
    facility = driver.find_element(
        "xpath", '/html/body/header/div/nav/ul/li[7]/a/span')
    facility.click()
    time.sleep(5000)


if __name__ == "__main__":
    main()
