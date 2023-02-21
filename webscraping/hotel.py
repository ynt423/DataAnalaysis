from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pyvirtualdisplay import Display

""" This project can base on user input to scrap to relevant hotel price here """
""" The coming goal:
    1.send data into a csv file
    2.provide cusomized selection for user(find the cheapest/the most polpular hotel in somewhere) """


def user_input():
    print("----------------------------------------------")
    print("Welcome to trip.com hotel sort price platform")
    target = input("Please input destination/hotel name: ")
    return target
    """  time.sleep(3) """
    """ print("Please wait for seconds...We are searching for you") """


def scraping():
    # initiate webdriver and navigate to Trip.com
    a = user_input()
    option = webdriver.ChromeOptions()
    """ option.add_argument("--kiosk") """
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument('log-level=3')
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.trip.com/")

    # search for hotels in a specific location
    """ //*[@id="hotels-destination"] """
    search_box = driver.find_element(
        "xpath", '//*[@id="hotels-destination"]')

    """ search_box = driver.find_element_by_id("search-box-hotel") """
    search_box.send_keys(a)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)
    # first row of search
    search_row = driver.find_element(
        "xpath", '/html/body/div[1]/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/ul/li[1]/div/div[2]/div[1]/div/div')
    # wait for results to load
    search_row.click()
    time.sleep(1)
    """ /html/body/div[1]/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/ul/li[3]/div/div[1]/div/div[1]/i """
    """  """
    dropdown = driver.find_element(
        "xpath", '//*[@id="searchBoxCon"]/div/div/ul/li[3]/div/div[1]/i')
    dropdown.click()
    time.sleep(1)
    # wait for results to load
    """ /html/body/div[1]/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/ul/li[3]/div/div[1]/div/div[3]/div[4]/span """
    """ //*[@id="searchBoxCon"]/div/div/ul/li[3]/div/div[3]/div[4]/span """
    confirm_btn = driver.find_element(
        "xpath", '//*[@id="searchBoxCon"]/div/div/ul/li[3]/div/div[3]/div[4]/span')
    confirm_btn.click()
    time.sleep(1)
    # press search

    search_btn = driver.find_element(
        By.CLASS_NAME, 'search-btn-wrap')
    """ search_btn = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/ul/li[3]/div/div[3]/div') """
    search_btn.click()
    time.sleep(1)
    # sort price function
    sort_by_price = driver.find_element(
        "xpath", '/html/body/div[3]/section/article/div/section/ul/li[1]/article/div[2]/div/div/div/div[2]/span')
    sort_by_price.click()
    # wait for results to sort
    time.sleep(1)

    # print the name and price of the cheapest hotel
    """ /html/body/div[3]/section/article/div/section/ul/li[4]/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/span """

    """ # scanning not necessary
    for i in range(1):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) """

    hotelName = driver.find_elements(
        By.CLASS_NAME, "list-card-title")
    time.sleep(2)
    hotelPrices = driver.find_elements(By.ID, "meta-real-price")
    count = 1

    for p, n in zip(hotelPrices, hotelName):
        print(f'Hotel {count}:{n.text}Price:{p.text}')
        count += 1
    # close the browser
    time.sleep(10000)
    """ driver.quit() """


def dataManage():
    print("幾時落堂")


scraping()
