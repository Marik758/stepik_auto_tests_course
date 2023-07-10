from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *
import time

try:
    
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    def func(y):
        
        return log(abs(12*sin(y)))

    
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    c = func(x)

    

    #time.sleep(3)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(c)

    browser.execute_script("window.scrollBy(0, 110);")

    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()


    rad = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rad.click()

     # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)








finally:

    browser.quit()
    
