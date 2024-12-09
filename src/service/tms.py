from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def run():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://koritbs.cafe24.com/student/index.php")
    sleep(1)

    id = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr:nth-child(3) > td > input")
    id.send_keys("chlthdbs3451")
    password = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-0.border-top-0.bg-brown > td > input")
    password.send_keys("chlthdbs3451@")
    loginButton = driver.find_element(by=By.CSS_SELECTOR, value='body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-danger.border-top-0.bg-brown > td > div > div:nth-child(2) > button')
    loginButton.click()
    sleep(3)

    trainingButton = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr.hover.pointer > td:nth-child(4)')
    trainingButton.click()
    sleep(3)

    crawlingButton = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > ul > li:nth-child(10) > div')
    driver.execute_script("arguments[0].click();", crawlingButton)
    sleep(3)

    registrationButton = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > caption > div > div:nth-child(2) > div > a')
    driver.execute_script("arguments[0].click();", registrationButton)
    sleep(3)

    titleInput = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input')
    titleInput.send_keys("최소윤")
    contentInput = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.ck.ck-editor__main > div')
    contentInput.send_keys("최소윤")
    sleep(5)

    completeButton = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr.end > td > button')
    driver.execute_script("arguments[0].click();", completeButton)

    pass