from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)



    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys('Nikita')

    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys('Markin')

    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys('nsd@jd.dk')
    
    dir1 = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir1, 'файл7.txt')

    
    input4 = browser.find_element(By.CSS_SELECTOR, "#file")
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
