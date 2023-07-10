from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)




    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)



    r = x+y
    


    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.VALUE, str(r)).text.click()

    #select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.select_by_value(str(r))

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
