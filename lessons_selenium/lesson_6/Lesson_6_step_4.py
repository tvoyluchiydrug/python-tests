
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    input1.send_keys("Sasha")
    input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys("Gulin")
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
    input3.send_keys("Rostov")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
