import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(type(link))

try:
    browser.get("http://suninjuly.github.io/find_link_text")
    elem = browser.find_element(By.PARTIAL_LINK_TEXT, link)
    elem.click()
    input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    input1.send_keys("Sasha")
    input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys("Gulin")
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
    input3.send_keys("Rostov")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
