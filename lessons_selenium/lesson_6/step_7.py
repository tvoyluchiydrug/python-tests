import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
text = "Ответ"
link = "http://suninjuly.github.io/huge_form.html"

try:
    browser.get(link)
    elems = browser.find_elements(By.TAG_NAME, "input")
    for elem in elems:
        elem.send_keys(text)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
