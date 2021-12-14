import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(5)

try:

    driver.get("https://stepik.org/lesson/25969/step/12")
    time.sleep(10)

    form = driver.find_element_by_css_selector(".textarea")
    form.send_keys("get()")
    time.sleep(5)

    submit_button = driver.find_element_by_css_selector(".submit-submission")
    submit_button.click()
    time.sleep(5)
finally:
    driver.quit()
