from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def run():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.kyobo.com")
    sleep(1)

    searchinput = driver.find_element(by=By.CSS_SELECTOR, value='#searchKeyword')
    searchinput.send_keys("파이썬")
    sleep(2)

    searchButton = driver.find_element(by=By.CSS_SELECTOR, value='#welcome_header_wrap > div.header_inner > div > div.gnb_search_box > a')
    searchButton.click()
    sleep(5)
    pass
