# 爬取ig關鍵字圖片
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
from selenium.webdriver import Firefox
from selenium.webdriver import Edge

PATH = "C:/Users/Oscar Yu/Desktop/chromedriver_win32/chromedriver.exe"
""" PATH = "C:/Users/hibyby/Desktop/chromedriver_win32/chromedriver.exe" """
""" driver = webdriver.Chrome(PATH) """
driver = Firefox()


def main():
    my_html = driver.execute_script(
        "return document.getElementsByTagName('html')[0].innerHTML")
    driver.get("https://www.instagram.com/")

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    #login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    login = driver.find_element(
        "xpath", '//*[@id="loginForm"]/div/div[3]/button')

    username.clear()
    password.clear()
    username.send_keys('your username')
    password.send_keys('your password')
    login.click()

    # notification
    notification = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))
    )
    notification.click()

# search bar
    search_bar = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div'))
    )
    # '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
    search_bar.click()
    search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'))
    )
    # return key into search bar
    keyword = "#cat"
    search.send_keys(keyword)
    time.sleep(1)
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    search.send_keys(Keys.RETURN)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "x1i10hfl"))
    )
    # scanning
    for i in range(5):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    imgs = driver.find_elements(By.CLASS_NAME, "x1i10hfl")
    filename = "cat"
    path = os.path.join(keyword)

    if not os.path.exists(path):
        os.mkdir(path)

    count = 0
    for img in imgs:
        save_as = os.path.join(path, keyword + str(count) + '.jpg')
        """ print(img.get_attribute("src"))
        wget.download(img.get_attribute("src"), save_as) """
        count += 1


if __name__ == "__main__":
    main()
