import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()

try:
    browser.get(link)
    input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    input1.send_keys("Sasha")
    input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys("Gulin")
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
    input3.send_keys("Rostov")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()
finally:
    time.sleep(15)
    browser.quit()