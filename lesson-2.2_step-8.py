import os
from selenium import webdriver
import time
import math

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_css_selector(".form-group > [name=\"firstname\"]")
    firstname.send_keys("Ivan")
    lastname = browser.find_element_by_css_selector(".form-group > [name=\"lastname\"]")
    lastname.send_keys("Ivanov")
    email = browser.find_element_by_css_selector(".form-group > [name=\"email\"]")
    email.send_keys("test@test.tt")
    email = browser.find_element_by_css_selector(".form-group > [name=\"email\"]")
    email.send_keys("test@test.tt")
    file = browser.find_element_by_css_selector("input[type=\"file\"]")
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
